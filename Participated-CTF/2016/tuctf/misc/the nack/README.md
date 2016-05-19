#The Nack

**Category:** Misc
**Points:** 100

**Description:**

Exctract each packet stream data, attach them together and get the flag in GIF file

```python
import pyshark
cap = pyshark.FileCapture('file.pcapng')

output = open('output.gif', 'wb')

data = ''
for packet in cap:
    if packet.transport_layer == 'TCP':
        if packet.ip.src == '192.168.188.130':
             d = packet.data.data
             output.write(d[-8:].decode('hex'))
output.close()
```

flag is: ```TUCTF{this_transport_layer_is_a_syn}```