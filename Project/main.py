from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from azure.storage.blob import BlobServiceClient
import os
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = '#412saqwerT'  # Replace with a secret key for session encryption



@app.route('/', methods=['GET', 'POST'])
def send_signal():
    if request.method == 'GET':
        return 'request received'
    else:
        return 'error'
    
    
    
    
    
    
    
    
    
# @app.route('/')
# def index():
#     return render_template('popup.html')
# # Azure Storage
# connection_str = "DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net"
# container_name = "images"
# blob_service_client = BlobServiceClient.from_connection_string(connection_str)
# container_client = blob_service_client.get_container_client(container_name)

# @app.route('/', methods=['GET', 'POST'])
# def send_signal():
#     try:
#         # URL of the website to send the signal to
#         website_url = "192.168.1.254"
#         response = requests.get(website_url)
#         response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

#         # If API call is successful, return 'Signal Sent'
#         return jsonify({'message': 'Signal Sent'}), 200
#     except requests.exceptions.RequestException as e:
#         # If API call fails, return an error message
#         return jsonify({'error': str(e)}), 500




# @app.route('/', methods=['GET'])
# def example():
#     print("test")
#     return 'Hello, World!'

# @app.route('/')
# def trigger():
#     print("Test ")
#     try:
#         # Make API call to PC 1

#             # If API call is successful, return 'Triggered'
#             return jsonify({'message': 'Triggered'}), 200
#     except requests.exceptions.RequestException as e:
#             # If API call fails, return an error message
#             return jsonify({'error': str(e)}), 500
        

# @app.route('/',methods=['GET','POST'])
# def trigger():
#     print("Test ghcghgjvjvgjv")
#     try:
#         # Make API call to PC 1
#         if request.method == 'GET':
#             pc1_ip_address = "192.168.1.200"  # Replace with the actual IP address of PC 1
#             url = f"http://{pc1_ip_address}:5000"
#             data = request.get_json()
#             name=data.get('name')
#             print(name)
#             # dataraise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

#             # If API call is successful, return 'Triggered'
#             return jsonify({'message': 'Triggered'}), 200
#     except requests.exceptions.RequestException as e:
#             # If API call fails, return an error message
#             return jsonify({'error': str(e)}), 500
# # login page route
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'admin' and password == 'password':
#             session['logged_in'] = True
#             return redirect('/dashboard')
#         else:
#             return render_template('login.html', error='Invalid username or password')
#     else:
#         return render_template('login.html')


# # dashboard route
# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     devices = ['Ecolog1', 'Ecolog2', 'Ecolog3']
#     if 'logged_in' not in session or not session['logged_in']:
#         return redirect('/')

#     if request.method == 'POST' and 'button' in request.form:
#         return redirect('/live')
    
#     blob_list = container_client.list_blobs()
#     latest_blob = max(blob_list, key=lambda b: b.creation_time)
    
#     # Specify the new name for the file
#     new_file_name = "Forest_Fire.jpg"
#     local_path = os.path.join("Project/static/images/", new_file_name)
    
#     with open(local_path, "wb") as file:
#         blob_client = container_client.get_blob_client(latest_blob.name)
#         blob_data = blob_client.download_blob()
#         blob_data.readinto(file)
        
#     blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{latest_blob.name}"
#     return render_template('dashboard.html', deviceharu= devices)


# # live route
# @app.route('/live', methods=['GET', 'POST'])
# def live():
#     if 'logged_in' not in session or not session['logged_in']:
#         return redirect('/')
    
#     return render_template('live.html')

# # logout route
# @app.route('/logout')
# def logout():
    
#     session.pop('logged_in', None)
#     return redirect('/')


# @app.route('/trigger', methods=['GET','POST'])
# def trigger():
#     # Render the HTML template and pass the path name of the image
#     return render_template('trigger-page.html')

# @app.route('/image', methods=['GET','POST'])
# def image():
#     return render_template('image.html')

# @app.route('/api/open-popup', methods=['POST'])
# def open_popup():
#     # Code to handle opening the popup (e.g., logging, analytics, etc.)
#     print('Popup opened')
#     return 'Popup opened successfully', 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)





