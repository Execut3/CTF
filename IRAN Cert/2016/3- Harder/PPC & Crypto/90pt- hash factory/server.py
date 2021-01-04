#!/usr/bin/env python2

import socket
import threading
import time
import SocketServer
import base64
import hashlib
import binascii
import random
import base64
import string

HOST = "0.0.0.0"
PORT = 12345

hash_algorithm_list = ['md5', 'sha1']
total_rounds = 10

WELCOME_MSG = "\nWellcome to hash-factory. Here I make the best hashes in the world. But recently had a problem with my hashes and I need strings with the same hash for my production. Can you help me please? (Y/N)? \n"
DESCRIPTION_MSG = "\nCool. First let me describe what I want. Don't worry; In the right time, I will give you a Flag as a PRIZE.\n"
DESCRIPTION_MSG += "\nIn each level i ask you for a specific number of strings that could make the same hash. I don't care what characters you use, as long as they make the SAME HASH!.\n"
DESCRIPTION_MSG += "\nAnd for simplicity, pack all the strings in this format: 'base64-encoded of each string seperated with ,'.\nFor example if i asked you for 2 strings, pack them like this for me: 'c3RyaW5nMQ==,c3RyaW5nMg==\n'"
DESCRIPTION_MSG += "\nOh, I also forgot. In each level all strings should have one word in common which i will ask you for it.\n"

CHALLENGE_MSG = "\nlevel '{level}', I need {total_strings} strings that their {hash_algorithm} is the same. They all should have the word \"{common_word}\"\n"
ERROR_MSG = "Sorry, but something is not right. Please verify your input and try again.\n"
CORRECT_MSG = "Right\n"
WRONG_MSG = "Wrong, See you later.\n"

flag = "APACTF{H0W_D!D_you_DO_7h47}"
FLAG_MSG = "Thank you. You really helped me . I owe you a flag: {flag}".format(flag=flag)


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # try:
        self.request.sendall(WELCOME_MSG)
        answer = self.request.recv(10)
        print answer
        if answer.strip() != 'Y':
            return
        self.request.sendall(DESCRIPTION_MSG)
        
        for level in range(total_rounds):
            hash_algorithm = hash_algorithm_list[random.randint(0,1)]
            string_numbers = random.randint(2, 6)
            common_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            self.request.sendall(CHALLENGE_MSG.format(level=level, total_strings=string_numbers, hash_algorithm=hash_algorithm, common_word=common_word))
            
            answer = self.request.recv(2048).strip()
            if not answer:
                self.request.sendall('\nAhhh. Never mind\n')
                return

            
            status = self.fetch_result(answer, common_word, string_numbers, hash_algorithm)
            
            if status:
                self.request.sendall(CORRECT_MSG)
            else:
                self.request.sendall(WRONG_MSG)
                return
            
        if level == total_rounds:
            self.request.sendall(FLAG_MSG)

        # except:
        #     return
        
    def recv_line(self):
        print 'here'
        result = ''
        buffer = self.request.recv(1)
        print buffer
        while not buffer in ['\n', '\r']:
            result += buffer
            buffer = self.request.recv[1]
        return result

    def generate_hash(self, msg, hash_algorithm='md5'):
        m = hashlib.md5()
        m.update(msg)
        return m.hexdigest()

    def fetch_result(self, answer, common_word, string_numbers, hash_algorithm):
        try:
            answer = answer.split(',')
            if len(answer) != string_numbers:
                return False
            tmp = []
            for a in answer:
                try:
                    tmp.append(base64.b64decode(a))
                except:
                    return False
                s_list = []
                for t in tmp:
                    if not common_word in t:
                        return False
                    if not t in s_list:
                        s_list.append(t)
                if len(s_list) == string_numbers:
                    hash1 = self.generate_hash(s_list[0].strip(), hash_algorithm)
                    for s in s_list[1:]:
                        if self.generate_hash(s.strip()) != hash1:
                            return False
                    return True
        except:
            return False
        return False
        

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = False
    server_thread.start()
    print 'there'

    while True:
        try:
            time.sleep(1)
        except:
            break

    server.shutdown()
    server.server_close()
