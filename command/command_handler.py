from key_generation import keys_generation
from encryption import encryption
from decryption import decryption
from registration import data_base
from language import language

def do_key(command):
    if data_base.check_registration():
        user_name = input(language.language()['command_handler']['name'])
        password = input(language.language()['command_handler']['password'])
        user = data_base.data_base(user_name, password)
        if user.login():
            command = command[1:]
            size = 1024
            if len(command) > 0:
                command[-1] = int(command[-1])
                if type(command[-1]) == int:
                    size = command[-1]
            keys_generation.async_keys_generation(size)
            return language.language()['command_handler']['do_key']['keys_in']
        elif not user.login():
            return language.language()['command_handler']['data_incorrectly']
    else:
        return language.language()['command_handler']['do_key']['false_reg']

def do_enc(command):
    command = command[1:]
    try:
        return encryption.async_encryption(command[-1])
    except IndexError:
        return language.language()['command_handler']['do_enc']['no_path']

def do_dec(command):
    if data_base.check_registration():
        user_name = input(language.language()['command_handler']['name'])
        password = input(language.language()['command_handler']['password'])
        user = data_base.data_base(user_name, password)
        none_file = False
        if user.login():
            command = command[1:]
            if len(command) > 1:
                if '-p' == command[0]:
                    none_file = True
                else:
                    none_file = 2
            try:
                return decryption.async_decryption(command[-1], none_file)
            except IndexError:
                return language.language()['command_handler']['do_dec']['no_path']
        elif not user.login():
            return language.language()['command_handler']['data_incorrectly']
    else:
        return language.language()['command_handler']['do_dec']['false_reg']
    
def do_reg():
    user_name = input(language.language()['command_handler']['name'])
    password = input(language.language()['command_handler']['password'])
    user = data_base.data_base(user_name, password)
    return user.create_db_and_registration()

def do_switch_language(command):
    language_list = ['ru', 'en']
    command = command[1:]
    if command[0] in language_list:
        language_file = open('logs/user.conf', 'w', encoding='utf-8')
        language_file.write(command[0])
        language_file.close()
        return language.language()['command_handler']['do_switch_language']['language_changed']
    elif not command in language_list and command:
        return language.language()['command_handler']['do_switch_language']['not_language']
    else:
        return language.language()['command_handler']['do_switch_language']['not_parameter']
        
def do_help():
    pass