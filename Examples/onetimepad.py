import random

class OneTimePad(object):
    """
    Implements basic one-time-pad functionality.
    
    Usage example:
        # 1. generate secret key
        secret_key = OneTimePad.genetate_key(20)    # for msgs of up to 20 chars
        print secret_key, OneTimePad.int2binstr(secret_key)

        # 2. build the one-time pad
        pad = OneTimePad(key=secret_key)

        # 3. Alice encrypts the message and sends ciphertext to Bob
        ciphertext = pad.encrypt('hi')

        # 4. Bob receives the ciphertext and decrypts
        decypt_msg = pad.decrypt(ciphertext)
    """
    
    def __init__(self, key):
        self.key = key

    def encrypt(self, msg):
        """Encrypts the string `msg` and prints its binary representation."""
        ctxt = ''
        for i, char in enumerate(reversed(msg)):
            k = (self.key >> 8*i) & 0b11111111
            enchar = ord(char) ^ k
            enchar_binstr = self.int2binstr(enchar)
            ctxt = enchar_binstr + ctxt
        return ctxt

    def decrypt(self, ctxt):
        """Decrypts the string of ciphertext `ctxt` and prints its message."""
        ctxt_length = len(ctxt)
        if ctxt_length % 8:
            raise ValueError('Expected ciphertext length to be a multiple of 8.')
        num_chars = ctxt_length/8
        msg = ''
        for j in range(0,num_chars):     # j is current index from the front
            i = num_chars - j -1         # i is current index from the back
            k = (self.key >> 8*i) & 0b11111111
            enchar_binstr = ctxt[8*j:8*(j+1):]
            msgchar = int(enchar_binstr, 2) ^ k
            msg = msg + chr(msgchar)
        return msg

    @staticmethod
    def genetate_key(max_length):
        """Generates a secret key big enough to encrypt stings up to `max_length`
           in lenght. Returns the secret key as an `int`."""
        return random.SystemRandom().getrandbits(max_length*8)

    @staticmethod
    def int2binstr(num):
        """Converts any integers to binary strings left-padded with zeros to nearest byte."""
        if num == 0:
            return '00000000'
        binstr = ''
        while num > 0:
            lsbyte = num & 0b11111111
            lsbyte_str = '{0:08b}'.format(lsbyte)
            binstr = lsbyte_str + binstr
            num = num >> 8
        return binstr

    @staticmethod
    def str2binstr(string):
        """Converts each character of `string` to ASCII binary representation."""
        binstr = ''
        for char in string:
            char_int = ord(char)
            char_binstr = '{0:08b}'.format(char_int)
            binstr += char_binstr
        return binstr


