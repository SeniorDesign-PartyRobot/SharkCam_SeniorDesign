from flask import Flask, render_template, url_for, Response
import cv2 as cv
import numpy as np
# Google Inits
from google.cloud import storage
from google.cloud.storage import Blob
from firebase import Firebase
import os
# error inits
import sys
import logging
# image inits
from PIL import Image
import glob
import pathlib

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
storageClient = storage.Client()

# trying cloud storage instead
# using this setup: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-client-libraries

def initializeBucket(bucketName):
    #initialize a storage client/check if bucket exists
    try: 
        
        bucket = storageClient.bucket(bucketName)
        bucket.storage_class = "COLDLINE"
        # only need to initialize once
        if not bucket.exists():
            new_bucket = storageClient.create_bucket(bucket, location="us")
            print("Created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))
        else:
            new_bucket = storageClient.get_bucket(bucketName)
        return new_bucket
    except:
        print('Error Message', file=sys.stderr)


def storeImage(imageLocation, bucketName):
    #now let's try an image in a specific folder that's already there
    # check if image exists
    if (os.path.isfile(imageLocation)):
        pass
    else:
        logging.warning("{} does not exist", imageLocation)
    try:
        path = pathlib.PurePath(imageLocation)
        
        bucket = storageClient.bucket(bucketName)
        blob = Blob(str(path.name.split(".")[0]), bucket) # file name without extension
        blob.upload_from_filename(imageLocation) # doesn't like this
        print(
            f"File {imageLocation} uploaded to {bucketName}."
        )
    except:
        logging.warning("Unsuccessful upload of {} to {}", imageLocation, bucketName)

def retrieveImage(destFolder, bucketName):
    # implement portion downloading (in case of interruption) later
    # portion downloading found here: https://cloud.google.com/storage/docs/downloading-objects#client-libraries-download-object
    # try:
        
        bucket = storageClient.bucket(bucketName)
        # make a list of all objects in bucket
        blobList = list(bucket.list_blobs())
        if (os.path.exists(destFolder)):
            pass
        else:
            os.makedirs(destFolder)

        for blobName in blobList:
            # blob = bucket.blob(blobName)
            print(blobName[0])
            # blob.download_to_filename(destFolder + "/" + blobName + ".jpg")
            # print("Downloaded image to {}".format(destFolder))
    # except:
        

def uploadImages(filePath, bucketName ): # upload all images in event folder to cloud storage
    imageList = [] # make a list of images
    for image in glob.glob(filePath + '*/.jpg'): # for every jpg in the folder, upload
        storeImage(filePath, image, bucketName )


# Main
def main():
    bucketName = "seniordesignbucket"
    imageLocation = "./testPhotos/testPic.jpg"
    imageName = "testImage.jpg"
    initializeBucket(bucketName)
    storeImage(imageLocation, bucketName)
    retrieveImage("downloadedImages", bucketName)
    return 0
main()