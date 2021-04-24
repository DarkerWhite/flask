from tcpclient import sendData
from tcpcommon import device, printT

from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/waterlu', methods=['POST'])
@cross_origin()
def result():
    print()
    recv = request.form['data']
    printT(f"received {recv}") # should display 'bar'
    echo = sendData(device["jpcn2"], recv, waitReply=True)
    printT(f"echo {echo}")
    return echo  # response to your request.
