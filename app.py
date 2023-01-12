from flask import Flask, render_template


app = Flask(__name__, template_folder="/app/templates")
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, threaded=True, port=5000)


while True:
    asdf= open('/app/templates/index.html', 'r')
    print("CONTENT OF HTML:" + str(asdf.read()) )
    asdf.close