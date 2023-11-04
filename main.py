import tqdm
from art import tprint
import tabulate
import os
from registration import data_base
import colorama
from command import command_handler
from encryption import encryption

run = True

while run:
    enter = input('>>> ').split()
    
    if enter[0] == 'key':
        print(command_handler.do_key(enter))
    if enter[0] == 'enc':
        print(command_handler.do_enc(enter))