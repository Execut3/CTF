from django.shortcuts import render_to_response
import argparse
from django.template import RequestContext

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vigener_square = {alphabet[x]: list(alphabet[x:] + alphabet[:x]) for x in range(len(alphabet))}
key = 'ctf'


def index(request):
    if request.method == "POST":
        plain = request.POST['plain']
        try:
            cipher = encrypt(key, plain)
        except:
            cipher = 'There was an error in your input...'
    return render_to_response('vigenere_index.html', locals(), RequestContext(request))


def encrypt(keyword, plaintext):
    global vigener_square
    global alphabet
    keyword = keyword.upper()
    plaintext = plaintext.lower().replace(' ', '')
    keytext = (keyword * ((len(plaintext)/len(keyword)) + 1))[:len(plaintext)]
    cipherlist = [alphabet.find(plaintext[i].upper()) for i in range(len(plaintext))]
    ciphertext = "".join([vigener_square[keytext[n]][cipherlist[n]] for n in range(len(plaintext))])
    return ciphertext


# def decrypt()
# # Create command line argument parser
# parser = argparse.ArgumentParser(description = "Enciphers or Deciphers text using the Vigenere Cipher")
# group = parser.add_mutually_exclusive_group(required = True)
# group.add_argument("-e", "--encipher", action = "store_true", help = "Encipher plaintext into CIPHERTEXT")
# group.add_argument("-d", "--decipher", action = "store_false", help = "Decipher CIPHERTEXT into plaintext")
# args = parser.parse_args()
#
# # Create Vigenere Square
#
#
#
# if args.encipher:
#
#
# else:
#     keyword = raw_input("Enter Keyword: ").upper()
#     ciphertext = raw_input("Enter CIPHERTEXT: ").upper()
#     keytext = (keyword * ((len(ciphertext)/len(keyword)) + 1))[:len(ciphertext)]
#     cipherlist = [VIGENERE_SQUARE[keytext[i]].index(ciphertext[i]) for i in range(len(keytext))]
#     plaintext = "".join([ALPHABET[cipherlist[n]] for n in range(len(ciphertext))]).lower()
#     print "Key:        ", keytext
#     print "plaintext:  ", plaintext
#     print "CIPHERTEXT: ", ciphertext