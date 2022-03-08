from concurrent.futures import process
from dotenv import load_dotenv
import flask
import subprocess
import os

load_dotenv()
app = flask.Flask(__name__)
port = os.environ["PORT"]
wolTarget = os.environ["WOL_TARGET"]


@app.route('/wol-trigger', methods=['POST'])
def home():
    bashCmd = ["sudo", "/usr/sbin/etherwake", "-i", "wlan0", "-b", wolTarget]
    process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("Attempting to wake up the PC...")
    return "OK"


app.run(host="localhost", port=port)
