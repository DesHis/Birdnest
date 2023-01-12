from flask import Flask, render_template
import os

print("THE DIRECTORY "+str(os.getcwd()))

app = Flask(__name__,)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
        app.run(debug=True, threaded=True, port=5000,)
        app.config['TEMPLATES_AUTO_RELOAD'] = True