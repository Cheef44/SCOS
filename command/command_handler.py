from key_generation import keys_generation
from encryption import encryption
from decryption import decryption

def do_key(command):
    command = command[1:]
    size = 1024
    if len(command) > 0:
        command[-1] = int(command[-1])
        if type(command[-1]) == int:
            size = command[-1]
    keys_generation.async_keys_generation(size)
        
    return 'You keys in logs/'

def do_enc(command):
    command = command[1:]
    try:
        return encryption.async_encryption(command[-1])
    except IndexError:
        return 'A compulsory argument was not found. You did not enter the path to the file you want to encrypt'

def do_dec(command):
    command = command[1:]
    try:
        return decryption.async_decryption(command[-1])
    except IndexError:
        return 'A compulsory argument was not found. You did not enter the path to the file you want to decrypt'