import re

pattern = "[A-Z][a-z][0-9][0-9][\?%$@#\^\*\(\)\[\];:]"
regex = re.compile(pattern)

characters = 'abcdefghijklmnopqrstuvwxyz'
characters += characters.upper()
characters += '?%$#@!^&*()[]\\'


def all_matching_strings(alphabet, max_length, regex):
    """Find the list of all strings over 'alphabet' of length up to 'max_length' that match 'regex'"""
    
    if max_length == 0: return 
    
    L = len(alphabet)
    for N in range(1, max_length+1):
        indices = [0]*N
        for z in xrange(L**N):
            r = ''.join(alphabet[i] for i in indices)
            if regex.match(r):                
               yield(r)
    
            i = 0
            indices[i] += 1
            while (i<N) and (indices[i]==L):
                indices[i] = 0
                i += 1
                if i<N: indices[i] += 1
    return

for r in all_matching_strings(characters, 8, regex): 
    print r