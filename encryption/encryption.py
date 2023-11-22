from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import base64

def async_encryption(files):
    try:
        key_file = open('logs/public.pem', 'rb').read()
    except FileNotFoundError:
        return 'Not keys'
    try:
        file = open(files, 'rb').read()
        keys = RSA.import_key(key_file).public_key()
        encrypt = PKCS1_OAEP.new(keys)
        encrypt = encrypt.encrypt(file)
        file_encorypt = open(f'{files}.async_encrypt.txt', 'wb')
        file_encorypt.write(encrypt)
        return f'You text in "{files}.async_encrypt.txt"'
    except FileNotFoundError:
        return 'File not'