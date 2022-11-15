from flask import Flask, render_template, url_for, Response
import cv2 as cv
import numpy as np

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
def photoViewer():
    return render_template('photoViewer.html')

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

# with app.app.context():

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

# def livestream():
#     # CV2 functionality code from cv2 site
#     cap = cv.VideoCapture(0) # uses local camera feed
#     if not cap.isOpened():
#         print("Cannot open camera")
#         exit()
#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         # if frame is read correctly ret is True
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break
#         # Our operations on the frame come here
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#         # Display the resulting frame
#         cv.imshow('frame', gray)
#         if cv.waitKey(1) == ord('q'):
#             break
#     # When everything done, release the capture
#     cap.release()
#     cv.destroyAllWindows()
#     return render_template('controls.html')
