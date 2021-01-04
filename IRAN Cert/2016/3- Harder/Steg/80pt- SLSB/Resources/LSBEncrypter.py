__author__ = 'omrih'

# Consts
HEADER_SIZE = 54 # Header size of BMP
DELIMITER = "$" # Separator between number of characters and text

# User Configurations
TextToHide = "APACTF{7H!5_0n3_was_4_little_TRICKY}"
ImageFile = "lsb.bmp"
StegImageFile = "lsb1.bmp"

class LSBEncrypter(object):

    def __init__(self):
        self.image_byte_counter = 0
        self.new_image_data = ''
        self.original_image = ''
        self.text_to_hide = ''

    def open_image(self):
        # Open the image file
        with open(ImageFile, "rb") as f:
            self.original_image = f.read()

    # Reading first chunk of the file - we don't want to overwrite the header
    def read_header(self):
        for x in range(0, HEADER_SIZE):
            self.new_image_data += self.original_image[x]
            self.image_byte_counter += 1

    def hide_text_size(self):
        sz = len(self.text_to_hide)
        s_sz = str(sz)
        s_sz += DELIMITER # s_sz now equal to size of text to hide + Delimiter
        self.do_steg(s_sz)

    # Hides the text in the image.
    # Does that by replacing the bytes LSB (Least significant bit) to be our bit
    def do_steg(self, steg_text):

        # Goes through the text we want to hide, char by char
        for ch in range(0, len(steg_text)):

            current_char = steg_text[ch] # Gets current Char
            current_char_binary = '{0:08b}'.format(ord(current_char)) # Gets the binary value of current character

            # Goes through current char binary - bit by bit
            for bit in range(0, len(current_char_binary)):
                new_byte_binary = ''

                ### Overwriting the image's byte LSB with our current Bit

                # Gets the binary value of original image byte
                current_image_binary = '{0:08b}'.format(ord(self.original_image[self.image_byte_counter]))

                # Copies the first 7 bits (we want them to be the same)
                new_byte_binary = current_image_binary[:7]

                # Set the last bit to be our bit
                new_byte_binary += current_char_binary[bit]

                # Gets the new char value by it's binary
                new_byte = chr(int(new_byte_binary, 2))

                # Adds new byte to output
                self.new_image_data += new_byte
                self.image_byte_counter += 1

    def copy_rest(self):
        # Copies the what's left of the file
        self.new_image_data += self.original_image[self.image_byte_counter:]

    def close_file(self):
        with open(StegImageFile, "wb") as out:
            out.write(self.new_image_data)

    def run(self, stega_text):
        self.text_to_hide = stega_text
        self.open_image()
        self.read_header()
        self.hide_text_size()
        self.do_steg(self.text_to_hide)
        self.copy_rest()
        self.close_file()

def main():
    global TextToHide
    stega_instance = LSBEncrypter()
    stega_instance.run(TextToHide)
    print "Successfully finished hiding text"

if __name__ == '__main__':
	main()