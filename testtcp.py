from tcpclient import sendData
from tcpcommon import device, printT

print(sendData(device['jpcn2'], 'lulululutestjson', waitReply=True))
