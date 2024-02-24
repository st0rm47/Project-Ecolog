from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from azure.storage.blob import BlobServiceClient
import os
import requests
from flask_cors import CORS

def open_browser(url):
    # Check if the OS is Windows, macOS, or Linux and open the browser accordingly
    if os.name == 'nt':  # For Windows
        os.system(f'start {url}')
    elif os.name == 'posix':  # For macOS and Linux
        os.system(f'xdg-open {url}')
    else:
        print("Unsupported operating system.")

# Example usage
url = "http://192.168.101.4:5000/alert"
app = Flask(__name__)
CORS(app)
app.secret_key = '#412saqwerT'  # Replace with a secret key for session encryption

# Azure Storage
connection_str = "DefaultEndpointsProtocol=https;AccountName=ecologstorage;AccountKey=GcQyJX5gaXrgMV4zaIeIWGuuoubKuRp2E7vMmQl4kFP5qnyun1MfikOMVlclmICiaJK4r5+NdGe6+AStz89CFQ==;EndpointSuffix=core.windows.net"
container_name = "images"
blob_service_client = BlobServiceClient.from_connection_string(connection_str)
container_client = blob_service_client.get_container_client(container_name)

# login page route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

# dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    devices = ['Ecolog1', 'Ecolog2', 'Ecolog3']
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/')

    if request.method == 'POST' and 'button' in request.form:
        return redirect('/live')
    
    return render_template('dashboard.html', devices=devices)

# live route
@app.route('/live', methods=['GET', 'POST'])
def live():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/')
    
    return render_template('live.html')

# logout route
@app.route('/logout')
def logout():
    
    session.pop('logged_in', None)
    return redirect('/')

@app.route('/trigger', methods=['GET','POST'])
def trigger():
   
    blob_list = container_client.list_blobs()
    latest_blob = max(blob_list, key=lambda b: b.creation_time)
    
    # Specify the new name for the file
    new_file_name = "Forest_Fire.jpg"
    local_path = os.path.join("Project/static/images/", new_file_name)
    
    with open(local_path, "wb") as file:
        blob_client = container_client.get_blob_client(latest_blob.name)
        blob_data = blob_client.download_blob()
        blob_data.readinto(file)
        
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{latest_blob.name}"
    open_browser(url)
    return redirect('alert' )

@app.route('/alert', methods=['GET','POST'])
def alert():
     return render_template('trigger-page.html' )
    

@app.route('/image', methods=['GET','POST'])
def image():
    return render_template('image.html')
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)




