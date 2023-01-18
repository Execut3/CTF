def is_palindrome(string):
    result = True
    str_len = len(string)
    for i in range(0, int(str_len/2)): # you need to check only half of the string
        if string[i] != string[str_len-i-1]:
            result = False
            break
    return result

infile = open('input.txt', 'r').readlines()

result = ''
for i in infile:
    text = i.strip()
    temp = ''
    for t in range(len(text)):
        t_text = text[t:]
        #print t_text
        for j in range(len(t_text)):
            j_temp = t_text[:j]
            if is_palindrome(j_temp):
                temp = j_temp
        if len(temp) > len(result):
            result = temp

print result