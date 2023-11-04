from key_generation import keys_generation
from encryption import encryption

def do_key(command):
    command = command[1:]
    size = 1024
    async_key = False
    if '-a' in command:
        async_key = True
    if len(command) > 0:
        command[-1] = int(command[-1])
        if type(command[-1]) == int:
            size = command[-1]
    if async_key == True:
        keys_generation.async_keys_generation(size)
    elif async_key == False:
        keys_generation.sync_keys_generation(size)
        
    return 'You keys in logs/'

def do_enc(command):
    command = command[1:]
    async_enc = False
    if '-a' in command:
        async_enc = True
    try:
        if async_enc:
            encryption.async_encryption(command[-1])
            return f'You text in "{command[-1]}.async_encrypt"'
        else:
            return encryption.sync_encryption(command[-1])
    except IndexError:
        return 'A compulsory argument was not found. You did not enter the path to the file you want to encrypt'