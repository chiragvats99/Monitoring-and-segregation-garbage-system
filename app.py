from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("vehicle-type-recognition-sys-firebase-adminsdk-kid7m-35c0a64ce8.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': "vehicle-type-recognition-sys.appspot.com"
})

# Create a reference to the Firebase Storage
bucket = storage.bucket()

@app.route('/')
def index():
    # Get the reference to the response file
    blob = bucket.blob('responses/response.txt')
    
    try:
        # Download the content of the response file
        content = blob.download_as_string().decode('utf-8')
    except Exception as e:
        content = f"Error: {e}"

    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)