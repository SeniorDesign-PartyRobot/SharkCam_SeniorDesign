from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
#homepage has buttons that navigate to controls page and photo viewer page
def index():
   return render_template('index.html')

@app.route('/controls')
def controls():
    return '<h1>Controls Page!</h1>'

@app.route('/photoviewer')
def photoViewer():
    return '<h1>Photo Viewer Page!</h1>'

