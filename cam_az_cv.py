import cv2
import numpy as np
import datetime
from azure.storage.blob import BlobServiceClient
import requests

#Connection String and Container Name with the help of BlobServiceClient
connection_str = "DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net"
container_name = "images"

#Creating a blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_str)

#Creating a container client
container_client = blob_service_client.get_container_client(container_name)

#Open the camera
camera = cv2.VideoCapture(0)

#Click picture from camera
ret, image = camera.read()

#Resizing the image to send into database
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)

#Make the image a numpy array and reshape it to the model's input shape.
image = np.asarray(image, dtype=np.float32).reshape(1, 300, 300, 3)

#Normalize the image array
image = (image / 127.5) - 1
save_image = ((image[0] + 1) * 127.5).astype(np.uint8)

#Save the image in the current working directory
save_path = "captured_frame.jpg"
cv2.imwrite(save_path, save_image)

blob_name = f"Forest.jpg{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
with open(save_path, "rb") as data:
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(data)
    print("Image uploaded to the azure storage")
    
camera.release()
cv2.destroyAllWindows()

# Specify the Custom Vision API endpoint
prediction_endpoint = "https://centralindia.api.cognitive.microsoft.com/customvision/v3.0/Prediction/cc643bba-fedc-4779-a94e-78f61613c4d9/classify/iterations/Forest_Fire_Confirmatory/image"

# Specify the Custom Vision prediction key
prediction_key = '6ad80ba7215e48e5988a3d2742d5a7d6'

# Get the list of blobs in the container
blob_list = container_client.list_blobs()

# Sorting blobs by creation time
latest_blob = max(blob_list, key=lambda b: b.creation_time)

# Construct the blob URL
blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{latest_blob.name}"

# Send the latest image data directly to the Custom Vision API for classification
headers = {
    'Prediction-Key': prediction_key,
    'Content-Type': 'application/octet-stream'
}
blob_client = container_client.get_blob_client(latest_blob.name)
response = requests.post(prediction_endpoint, headers=headers, data=blob_client.download_blob().readall())

# Process the prediction response
if response.status_code == 200:
    predictions = response.json()['predictions']
    for prediction in predictions:
        print(f"Prediction: {prediction['tagName']}, Probability: {prediction['probability']:.2f}")
else:
    print("Prediction failed")
