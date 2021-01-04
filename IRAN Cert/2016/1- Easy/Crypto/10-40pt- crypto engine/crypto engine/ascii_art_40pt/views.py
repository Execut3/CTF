from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from random import randint, shuffle


CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'
CHARACTERS += CHARACTERS.upper()
CHARACTERS += '1234567890!@#$%^&*()-=_+{}'

char_mapper = {'!': 184, '#': 125, '%': 185, '$': 108, '&': 142, ')': 147, '(': 174, '+': 131, '*': 168, '-': 165, '1': 176, '0': 109, '3': 138, '2': 122, '5': 197, '4': 167, '7': 196, '6': 107, '9': 189, '8': 199, '=': 141, 'A': 135, '@': 194, 'C': 113, 'B': 152, 'E': 170, 'D': 182, 'G': 146, 'F': 180, 'I': 121, 'H': 143, 'K': 151, 'J': 126, 'M': 173, 'L': 139, 'O': 177, 'N': 190, 'Q': 191, 'P': 150, 'S': 161, 'R': 186, 'U': 153, 'T': 114, 'W': 124, 'V': 112, 'Y': 119, 'X': 198, 'Z': 162, '_': 164, '^': 103, 'a': 181, 'c': 144, 'b': 129, 'e': 158, 'd': 134, 'g': 169, 'f': 148, 'i': 128, 'h': 149, 'k': 132, 'j': 117, 'm': 160, 'l': 154, 'o': 133, 'n': 115, 'q': 111, 'p': 155, 's': 163, 'r': 140, 'u': 178, 't': 104, 'w': 159, 'v': 171, 'y': 106, 'x': 101, '{': 127, 'z': 156, '}': 123}

# char_mapper = {}
# for c in CHARACTERS:
#     while True:
#         rand_ = randint(100,200)
#         if not rand_ in char_mapper.values():
#             char_mapper[c] = rand_
#             break
# print char_mapper


def index(request):
    if request.method == "POST":
        plain = request.POST.get('plain', '')
        if plain:
            for p in plain:
                if not p in CHARACTERS:
                    return HttpResponse('Your string include wrong characters.')

            cipher = []
            for p in plain:
                cipher.append(encrypt(p))
            print cipher
            cipher = '-'.join(cipher)

    return render_to_response('ascii_art_index.html', locals(), RequestContext(request))


def encrypt(p):
    if p in char_mapper.keys():
        p_id = char_mapper[p]
        return create_cipher(p_id)
    return '00-00-00'


def create_cipher(num):
    i0 = randint(20, 50)
    i1 = randint(20, 50)
    i2 = num - i0 - i1
    r = [str(i0), str(i1), str(i2)]
    print r
    shuffle(r)
    print r
    return '-'.join(r)
