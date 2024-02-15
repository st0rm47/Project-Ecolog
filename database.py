#Creating a database in azure to send images from device
from azure.storage.blob import BlobServiceClient

#Create a string that contains the connection string
connection_str= "DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net"

#Creating a blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_str)

#Create name for our container
container_name = "images"

# Upload a file to the azure storage
local_file_path = "test.jpg"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=" 1.jpg")
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)


