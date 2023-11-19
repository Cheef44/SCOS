from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import base64

def async_decryption(files):
    try:
        key = open('logs/private.pem', 'rb').read()
    except FileNotFoundError:
        return 'Not keys'
    try:
        file = open(files, 'rb').read()
        private_key = RSA.import_key(key)
        decrypt = PKCS1_OAEP.new(private_key)
        decrypt = decrypt.decrypt(file)
        file_decrypt = open(f'{files}.async_decrypt.txt', 'w', encoding='utf-8')
        str_file = decrypt.decode('utf-8')
        file_decrypt.write(str_file)
        file_decrypt.close()
        return f'You text in "{files}.async_decrypt.txt"'
    except FileNotFoundError:
        return 'File not'