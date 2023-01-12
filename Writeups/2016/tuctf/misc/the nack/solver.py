import pyshark
cap = pyshark.FileCapture('file.pcapng')

output = open('output.gif', 'wb')

data = ''
for packet in cap:
    if packet.transport_layer == 'TCP':
        if packet.ip.src == '192.168.188.130':
            # print packet.tcp.stream
             d = packet.data.data
             # print d
             output.write(d[-8:].decode('hex'))
output.close()
