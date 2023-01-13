from flask import Flask

app = Flask(__name__,)
@app.route('/')
def index():
    page = open("index.html", "r")
    content = page.read()
    page.close()
    print("this cuh so "+content)
    return content


if __name__ == '__main__':
        app.run(threaded=True, port=5000)