from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from language import language
import os
import chardet

def async_decryption(files, none_file):
    encoding = 'charmap'
    try:
        key = open('logs/private.pem', 'rb').read()
    except FileNotFoundError:
        return language.language()['decrypt']['not_keys']
    try:
        directory = f'{files}'
        directory_files = os.listdir(directory)
        string_file = []
        for files in directory_files:
            file = open(f'{directory}/{files}', 'rb').read()
            private_key = RSA.import_key(key)
            decrypt = PKCS1_OAEP.new(private_key)
            decrypt = decrypt.decrypt(file)
            if len(directory_files) == 1:
                encoding = chardet.detect(decrypt)['encoding']
            string_file.append(decrypt.decode(encoding))
        if none_file == False:
            file_decrypt = open(f'{files}.async_decrypt.txt', 'w', encoding='utf-8')
            file_decrypt.write(string_file)
            file_decrypt.close()
            return language.language(files)['decrypt']['true_decrypt']
        elif none_file == True:
            files = ''.join(string_file)
            return files
        elif none_file == 2:
            return language.language()['decrypt']['not_flag']
    except FileNotFoundError:
        return language.language()['decrypt']['file_not']
    except ValueError:
        return language.language()['decrypt']['wrong_key']