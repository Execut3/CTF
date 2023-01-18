import socket

SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = 'Execut3'
CHANNEL = '#root-me_challenge'

IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IRC.connect((SERVER,PORT))
IRC.send("JOIN %s"%CHANNEL)

while (1):
    buffer = IRC.recv(1024)
    # print buffer
    IRC.send('25/2\n')
    print IRC.recv(1024)
    fds
    msg = string.split(buffer)
    if msg[0] == "PING": #check if server have sent ping command
        send_data("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg [1] == 'PRIVMSG' and msg[2] == NICKNAME:
        filetxt = open('/tmp/msg.txt', 'a+') #open an arbitrary file to store the messages
        nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
        message = ' '.join(msg[3:])
        filetxt.write(string.lstrip(nick_name, ':') + ' -> ' + string.lstrip(message, ':') + '\n') #write to the file
        filetxt.flush() #don't wait for next message, write it now!