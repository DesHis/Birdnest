from flask import Flask


chungus=0

app = Flask(__name__,)
@app.route('/')
def index():
    page = open("templates/index.html", "r")
    content = page.read()
    page.close()
    chungus+=1
    return chungus


if __name__ == '__main__':
        app.run(threaded=True, port=5000)