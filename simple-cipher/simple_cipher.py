import random
from itertools import cycle


class Cipher:
    def __init__(self, key=None):
        if key != None:
            self.key = key
        else:
            self.key = ''
            for _ in range(200):
                self.key += chr(random.randint(97, 122))


    def encode(self, text):
        result = ''
        key = cycle(self.key)
        for i in range(len(text)):
            substitute = ord(text[i]) + ord(next(key)) % 97
            if substitute > 122:
                encrypted_letter = 96 + substitute % 122
            else:
                encrypted_letter = substitute
            result += chr(encrypted_letter)
        return result 


    def decode(self, text):
        result = ''
        key = cycle(self.key)
        for i in range(len(text)):
            substitute = ord(text[i]) - ord(next(key)) % 97
            if substitute < 97:
                decrypted_letter = substitute + 26
            else:
                decrypted_letter = substitute
            result += chr(decrypted_letter)
        return result

