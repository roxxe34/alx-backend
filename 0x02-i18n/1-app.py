from flask import Flask
from flask import render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@app.route("/")
def hello():
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)