from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from language import language
import os

def async_encryption(files):
    try:
        key_file = open('logs/public.pem', 'rb').read()
    except FileNotFoundError:
        return language.language()['encryption']['not_keys']
    try:
        file = open(files, 'rb').read().rstrip()
        keys = RSA.import_key(key_file).public_key()
        count = 0
        c = 15
        h = 0
        os.mkdir(f'{files}_')
        for _ in file:
            if len(file.decode('utf-8').rstrip()) > 13:
                encrypt = PKCS1_OAEP.new(keys)
                encrypt = encrypt.encrypt(file[count:c+1])
                file_encorypt = open(f'{files}_/{files}{h}.async_encrypt.AES', 'wb')
                file_encorypt.write(encrypt)
                c += 15
                h += 1
                count += 15
            else:
                c = 0
                h = 0
                count = 0
                encrypt = PKCS1_OAEP.new(keys)
                encrypt = encrypt.encrypt(file)
                file_encorypt = open(f'{files}_/{files}{h}.async_encrypt.AES', 'wb')
                file_encorypt.write(encrypt)
        return language.language(files)['encryption']['true_encrypt']
    except FileNotFoundError:
        return language.language()['encryption']['file_not']
    except ValueError:
        return language.language()['encryption']['value_error']
    except FileExistsError:
        return language.language(files)['encryption']['fileexists']