from key_generation import keys_generation
from encryption import encryption
from decryption import decryption
from registration import data_base

def do_key(command):
    if data_base.check_registration():
        user_name = input('Enter your name: ')
        password = input('Enter your password: ')
        user = data_base.data_base(user_name, password)
        if user.login():
            command = command[1:]
            size = 1024
            if len(command) > 0:
                command[-1] = int(command[-1])
                if type(command[-1]) == int:
                    size = command[-1]
            keys_generation.async_keys_generation(size)
            return 'You keys in logs/'
        elif not user.login():
            return 'Data entered incorrectly'
    else:
        return 'You are not registered, enter the command "reg" and register'

def do_enc(command):
    command = command[1:]
    try:
        return encryption.async_encryption(command[-1])
    except IndexError:
        return 'A compulsory argument was not found. You did not enter the path to the file you want to encrypt'

def do_dec(command):
    if data_base.check_registration():
        user_name = input('Enter your name: ')
        password = input('Enter your password: ')
        user = data_base.data_base(user_name, password)
        if user.login():
            command = command[1:]
            try:
                return decryption.async_decryption(command[-1])
            except IndexError:
                return 'A compulsory argument was not found. You did not enter the path to the file you want to decrypt'
        elif not user.login():
            return 'Data entered incorrectly'
    else:
        return 'You are not registered, enter the command "reg" and register'
    
def do_reg():
    user_name = input('Enter your name: ')
    password = input('Enter your password: ')
    user = data_base.data_base(user_name, password)
    return user.create_db_and_registration()