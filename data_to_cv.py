import requests
from azure.storage.blob import BlobServiceClient
import datetime

# Azure Blob Storage connection string
connect_str = 'DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net'

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Get the container client
container_name = 'images'
container_client = blob_service_client.get_container_client(container_name)

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
