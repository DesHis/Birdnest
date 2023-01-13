from flask import Flask

app = Flask(__name__,)
@app.route('/')
def index():
    return str(open("templates/index.html", "r").read())


if __name__ == '__main__':
        app.run(threaded=True, port=5000)