__author__ = "Execut3"
import re
import operator
import socket
import itertools


address = 'misc.chal.csaw.io'
port = 8001
sock = socket.socket()
sock.connect((address,port))


def splitkeepsep(s, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])


def find_regex_list(regex):
    reg_list = []
    r2 = re.findall(r"(((\[([A-Za-z0-9_\.\\*-]+)\])|(\(([A-Za-z0-9_\\*-|\.]+)\))|([A-Z\.a-z0-9_\\-]+)|[a-zA-Z]{1})((\*)|(\{[0-9]+\})|(\+))?)", regex)
    for i in r2:
        if i:
            reg_list.append(i[0])
    
    reg_result = []
    for j in reg_list:
        r1 = re.findall(r"[\[\(]+.", j)
        if r1:
            reg_result.append(j)
            continue
        r2 = re.findall(r"(([a-zA-Z\.0-9\-]+)\{?(\d+)?\}?)", j)
        if r2:
            try:
                string_len = int(r2[0][2])
                string = r2[0][1][:-1] + r2[0][1][-1]*string_len
            except:
                string_len = 1
                string = r2[0][1]
            reg_result.append(string) 
        else:
            reg_result.append(j)
    
    return reg_result


def brute_reg(regex):
    print regex
    for n in range(1,4):
        res = itertools.permutations('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_1',n) # 3 is the length of your result.
        for i in res: 
            word = ''.join(i)
            match = re.search(regex, word)
            # print match
            if match:
                return word
    return None


def read_line(sock):
    res = ''
    buffer = sock.recv(1)
    while buffer != '\n':
        res += buffer
        buffer = sock.recv(1)
    return res


def give_me_the_shit(reg_list):
    result = {}
    for reg in reg_list:
        len_of_string = 1

        # Finding the number of iterations
        r1 = re.findall(r"\{([0-9]+)\}|\+|\*", reg)
        if r1:
            try:
                len_of_string = int(r1[0])
            except:
                pass
        
        # [char-char]{*}
        r4 = re.findall(r"\[([\w\W-]+)\]", reg)
        if r4:
            tmp = r4[0][0] * len_of_string
            result[reg] = tmp
            continue
        
        # (string1|string2){*}
        r3 = re.findall(r"\(([a-zA-Z\.0-9]*)\|([a-zA-Z\.0-9]*)\)", reg)
        if r3:
            result[reg] = r3[0][1]*len_of_string
            continue
        
        result[reg] = reg
        
    return result


# We have the regex list of input (ready to brute)
print read_line(sock)
while True:
    regex = read_line(sock)
    regex = regex.replace('\\w','a').replace('\\W','-').replace('+','').replace('*','').replace('\\d','1').replace('\\D', 'a')
    reg_list = find_regex_list(regex)
    res_dict = give_me_the_shit(reg_list)
    print regex
    result = ''
    for i in reg_list:
        result += res_dict[i]
    print result
    
    sock.send(result + '\n')
    # print sock.recv(1024)
