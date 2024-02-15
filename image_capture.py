import cv2
import numpy as np
import time
import datetime
import requests
import argparse
import RPi.GPIO as GPIO
from azure.storage.blob import BlobServiceClient

detection_result = None

def camera():
    #Set up buzzer
    GPIO.setmode(GPIO.BCM)
    buzzer = 23
    GPIO.setup(buzzer, GPIO.OUT)
    
    #Azure Storage
    connection_str = "DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net"
    container_name = "images"
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_client = blob_service_client.get_container_client(container_name)
    
    #Open the camera
    camera = cv2.VideoCapture(0)
    ret, image = camera.read()
    image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 500, 500, 3)
    image = (image / 127.5) - 1
    save_image = ((image[0] + 1) * 127.5).astype(np.uint8)
    save_path = "Forest_Fire_Detected.jpg"
    cv2.imwrite(save_path, save_image) 
    camera.release()
    cv2.destroyAllWindows()
    
    #Send the data to Azure Storage and 
    blob_name = f"Forest_Fire_Detected.jpg {datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    with open(save_path, "rb") as data:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data)
        print("Image uploaded to the Azure Storage")
    
    #Custom Vision API
    prediction_endpoint = "https://centralindia.api.cognitive.microsoft.com/customvision/v3.0/Prediction/cc643bba-fedc-4779-a94e-78f61613c4d9/classify/iterations/Forest_Fire_Confirmatory/image"
    prediction_key = '6ad80ba7215e48e5988a3d2742d5a7d6'
    blob_list = container_client.list_blobs()
    latest_blob = max(blob_list, key=lambda b: b.creation_time)
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{latest_blob.name}"
    headers = {
        'Prediction-Key': prediction_key,
        'Content-Type': 'application/octet-stream'
    }
    blob_client = container_client.get_blob_client(latest_blob.name)
    response = requests.post(prediction_endpoint, headers=headers, data=blob_client.download_blob().readall())
    if response.status_code == 200:
        predictions = response.json()['predictions']
        detection_result = "Gunshot Detected"
        for prediction in predictions:
            if prediction ['probability'] >0.95:
                print("Forest Fire Detected")
                detection_result = "Forest Fire Detected"
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
    else:
        print("Error: ", response.status_code)
    
    #Send image to our website
    website_url = 'https://example.com/upload_image_endpoint'
    files = {'Image': open(save_path, 'rb')}
    data = {'Detection Result': detection_result}
    response = requests.post(website_url, files=files, data=data)
    if response.status_code == 200:
        print("Image sent to website successfully")
    else:
        print("Failed to send image to website")
    

    
