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
        file_encorypt = open(f'{files}.async_encrypt.txt', 'w')
        file_encorypt.write(base64.b64encode(encrypt).decode('utf-8'))
    except FileNotFoundError:
        return 'File not'

def sync_encryption(files):
    try:
        key_file = open('logs/sync_key.pem', 'rb').read()
    except FileNotFoundError:
        return 'Not keys'
    try:
        file = open(files, 'rb').read()
        encrypt = AES.new(key_file, AES.MODE_EAX)
        encrypt = encrypt.encrypt(file)
        file_encorypt = open(f'{files}.sync_encrypt.txt', 'wb')
        file_encorypt.write(base64.b64encode(encrypt).decode('utf-8'))
    except FileNotFoundError:
        return 'File not'