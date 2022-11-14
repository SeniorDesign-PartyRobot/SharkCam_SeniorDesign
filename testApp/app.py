from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
#homepage has buttons that navigate to controls page and photo viewer page
def index():
   return render_template('index.html')

@app.route('/controls')
def controls():
    return render_template('controls.html')

@app.route('/photoviewer')
def photoViewer():
    return render_template('photoViewer.html')

