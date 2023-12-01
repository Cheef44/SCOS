import tqdm
from art import tprint
import tabulate
import os
from registration import data_base
import colorama
from command import command_handler
from encryption import encryption
from decryption import decryption

run = True

try:
    while run:
        enter = input('>>> ').split()
        
        if enter[0] == 'key':
            print(command_handler.do_key(enter))
        if enter[0] == 'enc':
            print(command_handler.do_enc(enter))
        if enter[0] == 'dec':
            print(command_handler.do_dec(enter))
        if enter[0] == 'reg':
            print(command_handler.do_reg())
        if enter[0] == 'switchlan':
            print(command_handler.do_switch_language(enter))
except KeyboardInterrupt:
    print('Exit...')