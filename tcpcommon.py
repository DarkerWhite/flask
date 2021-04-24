import time
import json
import struct

bufferSize = 2048

device = {
    'taobo': ('172.17.9.43', 23333),
    'ras': ('172.25.24.188', 23333),
    'jpcn2' : ('160.116.119.240', 23333)
}

def getTime():
    return time.strftime("%Y-%m-%d %X")

def printT(text):
    print(f"[{getTime()}]: {text}")

def getJson(socket):
    # get json file
    jsonLength = struct.unpack(">I", socket.recv(4))[0]
    printT(f"Json length: {jsonLength}")
    jsonData = b""
    while len(jsonData) < jsonLength:
        data = socket.recv(min(bufferSize, jsonLength - len(jsonData)))
        if not data:
            printT("Error: receive data error.")
            return -1
            break
        jsonData += data
    jsonData = json.loads(jsonData.decode("utf-8"))
    return jsonData
