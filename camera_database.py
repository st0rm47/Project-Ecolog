import cv2
import numpy as np
import datetime
from azure.storage.blob import BlobServiceClient

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