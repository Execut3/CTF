__author__ = "Execut3"
import re
import operator
import socket


address = 'misc.chal.csaw.io'
port = 8001
sock = socket.socket()
sock.connect((address,port))


def splitkeepsep(s, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])


def find_regex_list(regex):
    reg_ex = regex
    reg_tmp = reg_ex
    
    # Split by []
    res_list = []
    r1 = re.findall(r"\(([A-Za-z0-9_\\*-|]+)\)", reg_ex)
    for i in r1:
        res_list.append('('+i+')')
        reg_tmp = reg_tmp.replace('('+i+')','')
    
    # Split by (){}
    r2 = splitkeepsep(reg_tmp, '*')
    for i in r2:
        m = re.findall(r"(\[([A-Za-z0-9_\\*-]+)\](\{\d\})?)", i)
        for j in m:
            res_list.append(j[0])      
    for i in res_list:
        reg_tmp = reg_tmp.replace(i,'')
    
    # Split by * and +
    r_star = splitkeepsep(reg_tmp, '*')
    for i in r_star:
        j = splitkeepsep(i, '+')
        for k in j:
            j = k.split('\\')
            for n in j:
                if n:
                    n = '\\'+n if 'W' in n else n
                    res_list.append(n)
    
    # Final list of regexs is in res_final list
    # print res_list
    
    order_dict = {}
    for i in res_list:
        order_dict[i] = reg_ex.find(i)
    
    
    sorted_x = sorted(order_dict.items(), key=operator.itemgetter(1))
    
    result = []
    for i in sorted_x:
        result.append(i[0])
    return result
 
    
def read_line(sock):
    res = ''
    buffer = sock.recv(1)
    while buffer != '\n':
        res += buffer
        buffer = sock.recv(1)
    return res


regex = 'Z*0*k(trump|cat)\W+[a-z](bernie|spider)[anwxTv\D9]{9}'
regex_list = find_regex_list(regex)

# We have the regex list of input (ready to brute)

while True:
    print read_line(sock)
    regex = read_line(sock)
    print regex
    reg_list = find_regex_list(regex)
    print reg_list