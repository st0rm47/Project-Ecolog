import cv2
import numpy as np
import time
import datetime
import requests
import argparse
import RPi.GPIO as GPIO
import webbrowser
from azure.storage.blob import BlobServiceClient

detection_result = None

def camera():
    # Set up buzzer
    GPIO.setmode(GPIO.BCM)
    buzzer = 23
    GPIO.setup(buzzer, GPIO.OUT)

    # Azure Storage
    connection_str = "your_connection_string_here`"
    container_name = "your_container_name_here"
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_client = blob_service_client.get_container_client(container_name)

    # Open the camera
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

    # Send the data to Azure Storage and
    blob_name = f"Forest_Fire_Detected {datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"
    with open(save_path, "rb") as data:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data)
        print("Image uploaded to Azure Storage")

    # Custom Vision API
    prediction_endpoint = "your_prediction_endpoint_here"
    prediction_key = 'your_prediction_key_here'
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
            if prediction['probability'] > 0.85:
                print("Forest Fire Detected")
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
                                                                                                              
                # Send API signal to website
                pc1_ip_address ="192.168.1.195" # IP address of the PC1
                url= f"http://{pc1_ip_address}:5000/trigger"

                response = requests.get(url)
                if response.status_code == 200:
                    print("Request sent successfully")
                    webbrowser.open_new_tab('http://192.168.1.195:5000/trigger')
                else:
                    print("Failed to send request")

    else:
        print("Error: ", response.status_code)
