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
            'true_encrypt': f'You text in "{files}_"',
            'file_not': "File not",
            'value_error': "The test exceeds the allowed number of characters",
            'fileexists': f"Unable to create file because it already exists: '{files}_'",
        },
        
        'command_handler': {
            
            'do_key':{
                'keys_in': 'You keys in logs/',
                'false_reg': 'You are not registered, enter the command "reg" and register',
            },
            'do_enc': {
                'no_path': 'A compulsory argument was not found. You did not enter the path to the file you want to encrypt',
                'no_parameter_t': "The '-t' parameter has not been entered",
                'no_parameter_f': "The '-f' parameter has not been entered",
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
            
            'do_help': [
                    "Commands:\n",
                    "reg - 'this command is used to register in the programme, has no parameters'\n",
                    "key - 'this programme is used to generate two keys, private and public. It has no parameters. Requires user data'\n",
                    "enc <file> 'this command is used to encrypt files. It has one mandatory parameter, the name of the file which must be in the root directory of the programme. It also has a second form of entry: enc -f <directory name where the encrypted files will be located> -t <text>'\n",
                    "dec -p <file>- 'this command decrypts a file, fa. It has a parameter, the name of the encrypted file that should be in the root directory, it also has an optional flag -p, this flag allows not to create a file with the decrypted text, but to output it at once'. switchlan <language> - 'this programme changes the language of the program. It has one mandatory parameter, language (en, ru)'\n"],
            
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
            'true_encrypt': f'Ваш текст в "{files}_"',
            'file_not': "Файла нет",
            'value_error': "Текст превышает допустимое количество символов",
            'fileexists': f"Невозможно создать файл, так как он уже существует: '{files}_'"
        },
        
        'command_handler': {
            
            'do_key':{
                'keys_in': 'Ваши ключи в logs/',
                'false_reg': 'Вы не зарегистрированы, введите команду «reg» и зарегистрируйтесь',
            },
            'do_enc': {
                'no_path': 'Обязательный аргумент не найден. Вы не ввели путь к файлу, который хотите зашифровать.',
                'no_parameter_t': "Параметр '-t' не был введен",
                'no_parameter_f': "Параметр '-f' не был введе",
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
            'do_help':[
                "Команды:\n",
                "reg - 'эта команда используется для регистрации в программе, не имеет параметров'\n",
                "key - 'эта программа используется для генерации двух ключей, закрытого и открытого. Не имеет параметров. Требуются данные пользователя'",
                "enc <file> - 'эта команда используется для шифрования файлов. Имеет один обязательный параметр - имя файла, который должен находиться в корневом каталоге программы. Также имеет вторую форму записи: enc -f <название директории в которой будут находится зашифрованные файлы> -t <текст>'\n",
                "dec -p <file>- 'эта команда расшифровывает файл, fa. У нее есть параметр - имя зашифрованного файла, который должен находиться в корневом каталоге, также есть необязательный флаг -p, этот флаг позволяет не создавать файл с расшифрованным текстом, а выводить его сразу'\n",
                "switchlan <language> - 'эта программа изменяет язык программы. У нее есть один обязательный параметр - язык (en, ru)'\n"],
            
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