from flask import Flask

app = Flask(__name__,)
@app.route('/')
def index():
    return str(open("templates/index.html", "r").read())


if __name__ == '__main__':
        app.jinja_env.auto_reload = True
        app.config["TEMPLATES_AUTO_RELOAD"] = True
        app.config["FLASK_RUN_EXTRA_FILES"] = True
        app.config['ENV'] = 'development'
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.run(threaded=True, port=5000)