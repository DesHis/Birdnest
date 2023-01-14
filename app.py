from flask import Flask, render_template
import subprocess
import threading


def runBirdnest():
    subprocess.call(['python', 'birdnest.py'])

app = Flask(__name__,)
@app.route('/')
def index():
    page = open("templates/index.html", "r")
    content = page.read()
    page.close()
    #return render_template("index.html")
    return content


if __name__ == '__main__':
    thread=threading.Thread(target=runBirdnest)
    thread.start()
    app.run(threaded=True, port=5000)