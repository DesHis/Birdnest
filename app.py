from flask import Flask, render_template

app = Flask(__name__,)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
        app.jinja_env.auto_reload = True
        app.config["TEMPLATES_AUTO_RELOAD"] = True
        app.config["FLASK_RUN_EXTRA_FILES"] = True
        app.config['ENV'] = 'development'
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.run(threaded=True, port=5000)