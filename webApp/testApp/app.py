from flask import Flask, render_template, url_for, Response
import cv2 as cv
import numpy as np
# Google Inits
from google.cloud import storage
from firebase import Firebase
import os
# photo inits
from PIL import Image, ImageShow


# Firebase Config
# add firebase to application : https://pypi.org/project/firebase/
#For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyBdKaaG7FDF7YovzMAJxeX55D-n4wRoTgM",
  "authDomain": "sharkcamapp.firebaseapp.com",
  "projectId": "sharkcamapp",
  "storageBucket": "sharkcamapp.appspot.com",
  "messagingSenderId": "416897826819",
  "appId": "1:416897826819:web:21ee93949de0c9fcfd4e36",
  "measurementId": "G-5Y35RKDW7F",
  "storageBucket": "gs://sharkcamapp.appspot.com",
  "databaseURL": ""
}

firebase = Firebase(firebaseConfig)


# init cloud storage
os.environ["GCLOUD_PROJECT"] = "SharkCamApp"

# trying cloud storage instead
# using this setup: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-client-libraries


bucketName = "test_bucket_soupstyle"
def initializeBucket():
    #initialize a storage client
    storageClient = storage.Client()
    bucket = storageClient.bucket(bucketName)
    bucket.storage_class = "COLDLINE"
    # only need to initialize once
    new_bucket = storageClient.create_bucket(bucket, location="us")
    print("Created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))
    return new_bucket

def storeImage():
    #now let's try an image in a specific folder that's already there
    imageName = "testPhotos/testPic.jpg"
    # is this initialization already done above? How can I make these universal?
    storageClient = storage.Client()
    bucket = storageClient.bucket(bucketName)
    blob = bucket.blob("testImage")
    blob.upload_from_filename(imageName)
    print(
        f"File {imageName} uploaded to testImage."
    )
    
    

def dispImage():
    # pull the image 
    photoRef = db.collection('photoTest').document('photo')
    photo = photoRef.get()
    if photo.exists:
        # get bytes as string
        # this is one way to get the bytes I think
        photoBytes = photo.to_dict()["imageData"]
        ImageShow.show(photoBytes)
        

        # convert to byte array
        # photoBytes = bytes(photoBytes, 'utf-8')
        # convert bytes to image
        # print(type(photoBytes))
        image = Image.frombytes("RGB",(1200,800), photoBytes)
        # image.save("./photoTestFromBytes")

# call the disp image function
def main():
    #initializeBucket()
    storeImage()
    return 0
main()

################################################### FLASK STUFF #################################################
app = Flask(__name__)

#webpages
@app.route('/', methods = ['GET', 'POST'])
#homepage has buttons that navigate to controls page and photo viewer page
def index():
   return render_template('index.html')

@app.route('/controls', methods = ['GET', 'POST'])
def controls():
    return render_template('controls.html')


@app.route('/photoviewer')
def photoViewer(image):
    return render_template('photoViewer.html',image=image)


# Controls
@app.route('/start', methods=['GET', 'POST'])
def start():
    start_message = "Robot has been started"
    print("started")
    return render_template('controls.html', message=start_message)

@app.route('/stop', methods=['GET', 'POST'])
def stop():
    stop_message = "Robot has been stopped"
    print("stopped")
    return render_template('controls.html', message=stop_message)

@app.route('/photomessage', methods=['GET','POST'])
def photoMessage():
    camera_message = "Camera is streaming"
    print("recording")
    return render_template('controls.html', message=camera_message)


#I know global variables are a sin
camera = cv.VideoCapture(0) #use local camera feed

def get_frames():
    while True:
        success, frame = camera.read()
        if not success: #if nothing happens, break
            break
        else:
            ret, image = cv.imencode('.jpg', frame)
            frame = image.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/livestream', methods=['GET','POST'])
def livestream():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def photoCapture():
    # only captures one frame on click
    ret, frame = camera.read()
    if not ret:
        print("no photo taken")
    else:
        ret, image = cv.imencode('.jpg', frame)
        frame = image.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  #decode frame

@app.route('/takephoto', methods=['GET','POST'])
def takePhoto():
    return Response(photoCapture(), mimetype='multipart/x-mixed-replace; boundary=frame')


# Settings def and functions
@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    return render_template('settings.html')

def sendScanCommand():
    #send an MQTT command to start the robot
    # for now, will run my own MQTT server to test functionality
    try:
        print("scan command sent")
    except:
        print("Scan command not sent")


