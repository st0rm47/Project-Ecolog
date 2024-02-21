

@app.route('/trigger', methods=['GET','POST'])
def trigger():
   
    blob_list = container_client.list_blobs()
    latest_blob = max(blob_list, key=lambda b: b.creation_time)
    
    # Specify the new name for the file
    new_file_name = "Forest_Fire.jpg"