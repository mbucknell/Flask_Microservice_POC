from flask import Flask

application = Flask(__name__)

from services import *

if __name__ == '__main__':
    application.run(debug=True)