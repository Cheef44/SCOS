def language(files=None):
    en = {
        'data_base': {
            'registered': "You're registered successfully.",
            'true_reg': "You're already registered.",
            'false_reg': "You're not registered.",
        },
        
        'decrypt': {
            'not_keys': "Not keys",
            'true_decrypt': f'You text in "{files}.async_decrypt.txt',
            'not_flag': 'You entered the wrong flag. There are flags: -p',
            'file_not': 'File not',
            'wrong_key': 'The file was encrypted using a different key',
        },
        
        'encryption': {
            'not_keys': "Not keys",
            'true_encrypt': f'You text in "{files}.async_encrypt.txt"',
            'file_not': "File not",
        },
        
        'command_handler': {
            
            'do_key':{
                'keys_in': 'You keys in logs/',
                'false_reg': 'You are not registered, enter the command "reg" and register',
            },
            'do_enc': {
                'no_path': 'A compulsory argument was not found. You did not enter the path to the file you want to encrypt',
            },
            'do_dec': {
                'no_path': 'A compulsory argument was not found. You did not enter the path to the file you want to decrypt',
                'false_reg': 'You are not registered, enter the command "reg" and register',
            },
            'do_switch_language': {
                'language_changed': 'Language changed',
                'not_language': 'This language is not supported in the program',
                'not_parameter': 'You have not entered a language',
            },
            
            'name': 'Enter your name: ',
            'password': 'Enter your password: ',
            'data_incorrectly': 'Data entered incorrectly',
        }
    }
    
    ru = {
        'data_base': {
            'registered': "Вы успешно зарегистрированы.",
            'true_reg': "Вы уже зарегистрированы.",
            'false_reg': "Вы не зарегистрированы.",
        },
        
        'decrypt': {
            'not_keys': "Нет ключей",
            'true_decrypt': f'Ваш текст в "{files}.async_decrypt.txt"',
            'not_flag': 'Вы ввели неправильный флаг. Есть флаги: -p',
            'file_not': 'Нет файла',
            'wrong_key': 'Файл был зашифрован с использованием другого ключа',
        },
        
        'encryption': {
            'not_keys': "Нет ключей",
            'true_encrypt': f'Ваш текст в "{files}.async_encrypt.txt"',
            'file_not': "Файла нет",
        },
        
        'command_handler': {
            
            'do_key':{
                'keys_in': 'Ваши ключи в logs/',
                'false_reg': 'Вы не зарегистрированы, введите команду «reg» и зарегистрируйтесь',
            },
            'do_enc': {
                'no_path': 'Обязательный аргумент не найден. Вы не ввели путь к файлу, который хотите зашифровать.',
            },
            'do_dec': {
                'no_path': 'Обязательный аргумент не найден. Вы не ввели путь к файлу, который хотите расшифровать',
                'false_reg': 'Вы не зарегистрированы, введите команду «reg» и зарегистрируйтесь',
            },
            'do_switch_language': {
                'language_changed': 'Язык изменен',
                'not_language': 'Этот язык не поддерживается в программе',
                'not_parameter': 'Вы не ввели язык',
            },
            
            'name': 'Введите ваше имя: ',
            'password': 'Введите ваш пароль: ',
            'data_incorrectly': 'Данные введены неверно',
        }
    }
    
    file = open('logs/user.conf', 'r', encoding='utf-8')
    file = file.read()
    
    if 'en' in file:
        output_phrases = en
    elif 'ru' in file:
        output_phrases = ru
    else:
        output_phrases = en
        
    return output_phrases