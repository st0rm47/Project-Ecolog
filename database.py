#Creating a database in azure to send images from device
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobServiceClient

#Create a string that contains the connection string
connection_str= ""

#Creating a blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_str)

#Create name for our container
container_name = "images"

# Create a string that contains the connection string
connection_str = "<your_connection_string>"

# Create a blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_str)

# Create a name for your container
container_name = "images"

# Upload a file to the azure storage
local_file_path = "<path_to_local_file>"
blob_client = blob_service_client.get_blob_client(container=container_name, blob="<blob_name>")
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)


