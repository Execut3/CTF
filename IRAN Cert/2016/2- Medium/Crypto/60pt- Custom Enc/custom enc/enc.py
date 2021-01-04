# flag = "xxxxxxxxxxxxxxxxxxxx"

prefix="Hello. Your flag is APACTF{"
suffix="}."
main_string="c an u br ea k th is we ir d en cr yp ti on".split()

clear_text = prefix + flag + suffix
enc_text = ""
for letter in clear_text:
    c1 = ord(letter) / 16
    c2 = ord(letter) % 16
    enc_text += main_string[c1]
    enc_text += main_string[c2]

print enc_text

