from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from language import language
import os

def async_encryption(files, none_file):
    try:
        key_file = open('logs/public.pem', 'rb').read()
    except FileNotFoundError:
        return language.language()['encryption']['not_keys']
    try:
        if none_file == True:
            text = files['text'].encode('utf-8')
            file = files['file']
        else:
            text = open(files, 'rb').read().rstrip()
        keys = RSA.import_key(key_file).public_key()
        count = 0
        c = 15
        h = 0
        print(text)
        os.mkdir(f'{file}_')
        for _ in text:
            if len(text.rstrip()) > 45:
                encrypt = PKCS1_OAEP.new(keys)
                encrypt = encrypt.encrypt(text[count:c+1])
                file_encorypt = open(f'{file}_/{file}{h}.async_encrypt.AES', 'wb')
                file_encorypt.write(encrypt)
                c += 15
                h += 1
                count += 15
            else:
                c = 0
                h = 0
                count = 0
                encrypt = PKCS1_OAEP.new(keys)
                encrypt = encrypt.encrypt(text)
                file_encorypt = open(f'{file}_/{file}{h}.async_encrypt.AES', 'wb')
                file_encorypt.write(encrypt)
        return language.language(file)['encryption']['true_encrypt']
    except FileNotFoundError:
        return language.language()['encryption']['file_not']
    except ValueError:
        return language.language()['encryption']['value_error']
    except FileExistsError:
        return language.language(file)['encryption']['fileexists']