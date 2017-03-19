import numpy
def encryption (message, key):
    ret = ""
    for char in message:
        if not char.isalpha():
            continue
        ret += chr(((ord(char) - ord('a') + int(key)) % 26) + ord('a'))
    return ret

def keyof(s):
  ret = 0
  for i in s:
    ret = ord(i) + ret
  return ret;

msg_z = "XXX" # Flag was placed here. Just to remind you.
n = 100000000

key = keyof(msg_z)
msg = encryption(msg_z,key)

for i in range(n):
  new_msg = encryption(msg,key)
  key = keyof(msg)
  msg = new_msg
  print str(i*100.0/n) + "%"


print msg