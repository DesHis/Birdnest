from flask import Flask

app = Flask(__name__,)
@app.route('/')
def index():
    page = open("templates/index.html", "r")
    content = page.read()
    page.close()
    return str(open("templates/index.html", "r"))


if __name__ == '__main__':
        app.run(threaded=True, port=5000)