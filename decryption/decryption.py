from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import base64
from language import language

def async_decryption(files, none_file):
    try:
        key = open('logs/private.pem', 'rb').read()
    except FileNotFoundError:
        return language.language()['decrypt']['not_keys']
    try:
        file = open(files, 'rb').read()
        private_key = RSA.import_key(key)
        decrypt = PKCS1_OAEP.new(private_key)
        decrypt = decrypt.decrypt(file)
        str_file = decrypt.decode('utf-8')
        if none_file == False:
            file_decrypt = open(f'{files}.async_decrypt.txt', 'w', encoding='utf-8')
            file_decrypt.write(str_file)
            file_decrypt.close()
            return language.language(files)['decrypt']['true_decrypt']
        elif none_file == True:
            files = str_file
            return files
        elif none_file == 2:
            return language.language()['decrypt']['not_flag']
    except FileNotFoundError:
        return language.language()['decrypt']['file_not']
    except ValueError:
        return language.language()['decrypt']['wrong_key']