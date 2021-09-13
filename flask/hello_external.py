"""
Minimal example using Flask (Flask's Hello World application) with external access
page 419
To find ip run 'ipconfig'
from cmd line run python3 hello_external.py
c:/user/rokvcddd/Anconda3/python3.exe
"""

# Import required packages:
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World2222!"


if __name__ == "__main__":
    # Add parameter host='0.0.0.0' to run on your machines IP address:
    app.run(host='0.0.0.0')
