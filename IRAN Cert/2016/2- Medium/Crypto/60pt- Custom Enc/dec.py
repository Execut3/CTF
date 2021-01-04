#!/usr/bin/env python

BASE = "c an u br ea k th is we ir d en cr yp ti on".split()
def chunks(l, n=1):
    for i in xrange(0, len(l), n):
        yield l[i:i+2]

def main():
    message = raw_input("msg> ")
    tokens = []
    chunks_gen = chunks(message)
    for cyphered_nibble in chunks_gen:
        if cyphered_nibble in BASE:
            tokens.append(cyphered_nibble)
            chunks_gen.next()
        else:
            tokens.append(cyphered_nibble[0])

    final_string = ""
    for cyphered_letter in chunks(tokens, n=2):
        if len(cyphered_letter) == 2:
            char1, char2 = cyphered_letter[0], cyphered_letter[1]
            ascii_letter = 16 * BASE.index(char1) + BASE.index(char2)
        else:
            char1 = cyphered_letter[0]
            ascii_letter = 16 * BASE.index(char1)
        try:
            letter = chr(ascii_letter)
        except ValueError:
            letter = "."
        finally:
            final_string += letter

    print final_string
    print repr(final_string)

if __name__ == '__main__':
    main()