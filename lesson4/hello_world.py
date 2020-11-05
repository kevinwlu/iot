from flask import Flask
from flask import send_from_directory
import os
app = Flask(__name__)

@app.route("/")
def hello():
    """
    Decor function which returns a function

    Args:
    """
    return "Hello World!"

@app.route('/favicon.ico')
def favicon():
    """
    Return favicon file

    Args:
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', 
                               mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()
