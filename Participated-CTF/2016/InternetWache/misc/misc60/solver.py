__author__ = 'Execut3'
import base64

cipher = open('README.txt', 'r').read()
cipher = cipher.split('\n')
baseline_len = len(cipher[0])

cipher_sections = []
tmp = ''
for i in cipher:
    tmp += i.strip()
    if len(i) < baseline_len:
        cipher_sections.append(tmp)
        tmp = ''

# Now we have all sections seperated in cipher_sections list
for i in cipher_sections:
    decoded = base64.b64decode(i)
    print decoded
    
print 'flag is: IW{QR_C0DES_RUL3}'