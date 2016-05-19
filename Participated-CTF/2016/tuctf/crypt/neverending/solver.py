import socket
import string
import time

Morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

cipher_dict_2 = {' ': '-', '$': '1', '(': '5', ',': '9', '0': '=', '4': 'A', '8': 'E',
                 '<': 'I', '@': 'M', 'D': 'Q', 'H': 'U', 'L': 'Y', 'P': ']', 'T': 'a',
                 'X': 'e', '\\': 'i', '`': 'm', 'd': 'q', 'h': 'u', 'l': 'y', 'p': '}',
                 't': '"', 'x': '&', '|': '*', '#': '0', "'": '4', '+': '8', '/': '<',
                 '3': '@', '7': 'D', ';': 'H', '?': 'L', 'C': 'P', 'G': 'T', 'K': 'X',
                 'O': '\\', 'S': '`', 'W': 'd', '[': 'h', '_': 'l', 'c': 'p', 'g': 't',
                 'k': 'x', 'o': '|', 's': '!', 'w': '%', '{': ')', '"': '/', '&': '3',
                 '*': '7', '.': ';', '2': '?', '6': 'C', ':': 'G', '>': 'K', 'B': 'O',
                 'F': 'S', 'J': 'W', 'N': '[', 'R': '_', 'V': 'c', 'Z': 'g', '^': 'k',
                 'b': 'o', 'f': 's', 'j': 'w', 'n': '{', 'r': ' ', 'v': '$', 'z': '(',
                 '~': ',', '!': '.', '%': '2', ')': '6', '-': ':', '1': '>', '5': 'B',
                 '9': 'F', '=': 'J', 'A': 'N', 'E': 'R', 'I': 'V', 'M': 'Z', 'Q': '^',
                 'U': 'b', 'Y': 'f', ']': 'j', 'a': 'n', 'e': 'r', 'i': 'v', 'm': 'z',
                 'q': '~', 'u': '#', 'y': "'", '}': '+'}

cipher_dict_31 = {'1': '1', '0': '0', '3': '3', '2': '2', '5': '5', '4': '4', '7': '7', '6': '6', '9': '9', '8': '8', '=': '=', 'A': 'A', 'C': 'C', 'B': 'B', 'D': 'S', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'f', 'd': 's', 'g': 'd', 'f': 't', 'i': 'u', 'h': 'h', 'k': 'e', 'j': 'n', 'm': 'm', 'l': 'i', 'o': 'y', 'n': 'k', 'q': 'q', 'p': ';', 's': 'r', 'r': 'p', 'u': 'l', 't': 'g', 'w': 'w', 'v': 'v', 'y': 'j', 'x': 'x', 'z': 'z'}

cipher_dict_32 = {'a': 'a', 'c': 'j', 'b': 'x', 'e': '.', 'd': 'e', 'g': 'i', 'f': 'u', 'i': 'c', 'h': 'd', 'j': 'h', '1': '1', '0': '0', '3': '3', '2': '2', '5': '5', '4': '4', '7': '7', '6': '6', '9': '9', '8': '8', '=': ']'}

cipher_dict_5 = {'A': '^', 'C': '\\', 'B': ']', 'D': '[', 'p': '/', 's': ',', 'v': ')', 'y': '&', 'x': "'", 'w': '(', 'r': '-', 'u': '*', 'a': '>', 'q': '.', 'c': '<', 'b': '=', 'e': ':', 'd': ';', 'g': '8', 'f': '9', 'i': '6', 'h': '7', 'k': '4', 'j': '5', 'm': '2', 'l': '3', 'o': '0', 'n': '1', '1': 'n', '0': 'o', '3': 'l', '2': 'm', '5': 'j', '4': 'k', '7': 'h', '6': 'i', '9': 'f', '8': 'g', 'z': '%', 't': '+'}

send_key = '=' + string.printable[20:40]
send_key_5 = string.printable[20:40]

word_list = ['I OWE YOU', 'READING IS DANGEROURS', 'BASTIAN', 'TRY SWIMMING',
             'WELCOME ATREYU', 'THE NOTHING', 'MY LUCKDRAGON', 'ATREYU VS GMORK',
             'SAVE THE PRINCESS', 'THE ORACLE', 'FRAGMENTATION', 'MOON CHILD',
             'GIANT TURTLE', 'GMORKS COOL', 'DONT FORGET AURYN', 'READENG IS DANGEROURS',
             'DONT FORGET AIRYN', 'FRAGMANTATION', 'MY LOCKDRAGON', 'THE ORECLE',
             'GIENT TURTLE', 'CAVE THE PRENCESS', 'TRY CWIMMING', 'GNORKS COOL',
             'THE NUTHING', 'ARTEYU VS GNORK', 'I OWA YOU', 'BASTIEN', 'WELKOME ATREYU', 'MONO KHILD']

def find_num(i):
    splitted = i.split(' ')
    i_num = 0
    for j in range(len(splitted)):
        i_num = len(splitted[j]) + i_num*10*j    
    return i_num


word_numbers = []
for i in word_list:
    word_numbers.append(find_num(i))


def check_word(word):
    output = ''
    for w in word_list:
        if ''.join(word.split(' ')) in ''.join(w.split(' ')).lower():
            word = w.lower()
            return word
    if 'dangerours' in word:
        if 'eadeng' in word:
            output = 'readeng is dangerours'
        else:
            output = 'reading is dangerours'
        return output
    if 'thenothing' in word:
        return 'the nothing'
    
    for w in word_list:
        count = 0
        word_tmp = word.split(' ')
        w_tmp = w.split(' ')
        for i in range(len(word_tmp)):
            print word_tmp[i]
            for j in range(len(word_tmp[i])):
                try:
                    if word_tmp[i][j].lower() == w_tmp[i][j].lower():
                        count += 1
                except:
                    pass
        if count >= 5:
            output = w
            break
    return output


def receive_data(sock):
    data = ''
    buff = sock.recv(1)
    data = buff
    while buff != '\n':
        buff = sock.recv(1)
        data += buff
    return data


def to_morse(text):
    result = []
    for t in text:
        for key,value in Morse.items():
            if t == key:
                result.append(value)
                break
    return ' '.join(result)


def xor(s1, s2):
    res = [chr(0)]*len(s1)
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
        # print res
    res = ''.join(res)
    return res


address = '146.148.102.236'
port = 24069
s = socket.socket()
s.connect((address,port))

data = ''
Round = 1
while True:
    print '[*] Starting Round %i'%Round

    Stage = 1
    while Stage <= 50:
        print '[+] Stage %i'%Stage
        Stage += 1
        
        data = s.recv(8096)
        if Round == 7:
            print data
        
        sned_it = 'abcdefghijkl'
        if 'Give me some text' in data or not data:
            if Round == 3:
                s.send(''.join(send_key) + '\n')
            elif Round == 5:
                s.send(''.join(send_key_5) + '\n')
            else:
                s.send(sned_it + '\n')
        txt = s.recv(8096)
        if Round == 7:
            print txt

        txt = txt.split('\n')
        for t in txt:
            if 'What is' in t:
                txt_d = t.split('What is')[1].split('decrypted')[0].strip()
            elif 'encrypted' in t:
                txt_t = t.split('encrypted is')[1].split('\n')[0].strip()

        if Round == 3:
            if txt_t[0] == '=':
                for t in range(len(txt_t)):
                    if not t in cipher_dict_31.keys():
                        cipher_dict_31[send_key[t]] = txt_t[t]
            elif txt_t[0] == ']':
                for t in range(len(txt_t)):
                    if not t in cipher_dict_32.keys():
                        cipher_dict_32[send_key[t]] = txt_t[t]
        
        if Round == 5:
            for t in range(len(txt_t)):
                if not t in cipher_dict_5.keys():
                    cipher_dict_5[send_key_5[t]] = txt_t[t]

        if Round == 1:
            encrypted = txt_d.split('  ')
            decrypted = []
            for m_word in encrypted:
                d = ''
                for e in m_word.split(' '):
                    for key,value in Morse.iteritems():
                        if value == e:
                            d += key
                            break
                decrypted.append(d)
            decrypted = ' '.join(decrypted)
            if not decrypted.upper() in word_list:
                word_list.append(decrypted.upper())
                # print word_list
            s.send(decrypted+'\n')

        elif Round == 2:
            decrypted = ''
            for t in txt_d:
                for key,value in cipher_dict_2.iteritems():
                    if value.lower() == t.lower():
                        decrypted += key.lower()
                        break
            decrypted = check_word(decrypted)
            s.send(decrypted+'\n')

        elif Round == 3:
            decrypted = ''
            for t in txt_d:
                if txt_t[0] == '=':
                    for key,value in cipher_dict_31.iteritems():
                        if value.lower() == t.lower():
                            decrypted += key.lower()
                            break
                elif txt_t[0] == ']':
                    for key,value in cipher_dict_32.iteritems():
                        if value.lower() == t.lower():
                            decrypted += key.lower()
                            break
            tmp = decrypted
            decrypted = ''
            for j in word_list:
                if tmp in ''.join(j.split(' ')).lower():
                    decrypted = j.lower()
                    print 'decrypted is : %s'%decrypted
                    break
                if decrypted:
                    break
            s.send(decrypted+'\n')

        elif Round == 4:
            if len(txt_t) < len(sned_it):
                txt_t = ' '+txt_t
            index = ord(txt_t[0]) - ord(sned_it[0])

            decrypted = ''
            for i in txt_d:
                tmp = ord(i) - index
                if tmp > 126:
                    tmp -= 95
                if tmp < 32:
                    tmp += 95
                decrypted += chr(tmp)
        
            tmp = ''.join(decrypted.split(' '))
            decrypted = ''
            for j in word_list:
                if tmp in ''.join(j.split(' ')).lower():
                    decrypted = j.lower()
                    print 'decrypted is : %s'%decrypted
                    break
                if decrypted:
                    break
            s.send(decrypted+'\n')
            
        elif Round == 5:
            decrypted = ''
            for t in txt_d:
                for key,value in cipher_dict_5.iteritems():
                    if value.lower() == t.lower():
                        decrypted += key.lower()
                        break
            tmp = decrypted
            decrypted = ''
            for j in word_list:
                if tmp in ''.join(j.split(' ')).lower():
                    decrypted = j.lower()
                    print 'decrypted is : %s'%decrypted
                    break
                if decrypted:
                    break
            s.send(decrypted+'\n')
        
        elif Round == 6:
            a = sned_it
            b = txt_t
            
            distance = ord(b[0]) - ord(a[0])
            cipher_base = b[0]
            clear_base = a[0]
            
            step = ord(b[1]) - ord(b[0]) -1
            print step
            print distance
            level5_mapper = {}
            for i in 'abcdefghijklmnopqrstuvwxyz ':
                index = ord(i) - ord(clear_base)
                c =  ord(i)+distance+ index*step
                if c > 126:
                    c -= 95
                if c < 32:
                    c += 95
                c = c % 256
                level5_mapper[i] = chr(c)
            
            cipher = txt_d
            decrypted = ''
            for i in cipher:
                for key,value in level5_mapper.iteritems():
                    if value == i:
                        decrypted += key
            print decrypted
            
            tmp = ''.join(decrypted.split(' '))
            decrypted = ''
            for j in word_list:
                if tmp in ''.join(j.split(' ')).lower():
                    decrypted = j.lower()
                    print 'decrypted is : %s'%decrypted
                    break
                if decrypted:
                    break
                
            s.send(decrypted+'\n')
        elif Round == 7:
            print 'here'
            
    # data = recv_timeout(s)
    data = receive_data(s)
    data += receive_data(s)
    data += receive_data(s)
    data = data.split('\n')
    for d in data:
        if 'TUCTF' in d:
            flag = d
    print '[+++++] Flag for Round %i is: %s\n=====================\n'%(Round, flag)
    Round += 1

        