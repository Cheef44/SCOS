from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import base64
from language import language

def async_encryption(files):
    try:
        key_file = open('logs/public.pem', 'rb').read()
    except FileNotFoundError:
        return language.language()['encryption']['not_keys']
    try:
        file = open(files, 'rb').read()
        keys = RSA.import_key(key_file).public_key()
        encrypt = PKCS1_OAEP.new(keys)
        encrypt = encrypt.encrypt(file)
        file_encorypt = open(f'{files}.async_encrypt.txt', 'wb')
        file_encorypt.write(encrypt)
        return language.language(files)['encryption']['true_encrypt']
    except FileNotFoundError:
        return language.language()['encryption']['file_not']