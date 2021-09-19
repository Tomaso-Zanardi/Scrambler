# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:59:26 2021

@author: Tomaso Zanardi

"""
# in this testing environment we need some modules from the standard library,
# and some third party ones. lastly we need to import the functions of scrambler
import os
import re
import regex
from scrambler import *
from termcolor import colored, cprint
from most_elegant import *

# here are some warning messages and lists that will come in handy later
Q = colored('ATTENTION: press q and then (enter) if you want to end the program!', 'red')
warning_1 = colored('Warning: if the file is not in your working directory, specify the full path', 'red')
warning_2 = colored('Warning: be sure to name the new file with a name that is not already assigned to another file', 'red')
op = ['open', 'OPEN', 'Open','o','O']
sc = ['scramble', 'Scramble', 'SCRAMBLE','s','S']
first_choices = [op,sc]
second_choices = ['ALL', '1','2','3','4']
sv = ['save', 'SAVE', 'Save','s','S']
pt =['print', 'PRINT', 'Print','p','P']
third_choices = [sv,pt,'&']
#here is colorful a greeting message for the user
cprint('---------------------\n---------------------','red')
cprint('Hello there!\nWelcome to the SCRAMBLER testing environment.\nHere you can use the many features of text scrambler on a text that you input or on the text contained in a text file. in any case you can choose to save the scrambled text in a  new document if you wish!','red','on_cyan', attrs=['bold'])
cprint('---------------------\n---------------------','red')
cprint('---------------------\n---------------------','red')

# the user can choose to load a text from a file or to write a new text
print('tell me what to do:\n\n1)do you want to open a text file and scramble its content (open)\n2)do you want to scramble something you just come up with?(scramble)')

# if the choice is to load a text from a file the 'testo' variable will be assigned that text
choice_1 = 'xxx'
while choice_1 not in first_choices:
    choice_1 = input('')
    if choice_1 in op:
        file_name = input ('what is the name of the text file you want to scramble?\n' + warning_1 + '\n\n')
        f = open(file_name, 'r')
        testo = f.read()
        f.close()
        break
    # if the user decides to scramble a new text the 'testo' variable will be assigned an input string by the user        
    elif choice_1 in sc:
        testo = input('give me the text to scramble:\n\n')
        break
    else:
        cprint ('this option is not recognized! what do you want to do? (open\scramble)', 'red')
# here the user is proposed a new set of choices: which function from Scrambler to use, or to use them all
print ('\n\ntell me what you want to do with this text, here are your options:\n')
cprint('1) you can have your text scrambled for every letter but the first and the last of every word.\n', 'green', 'on_cyan')
cprint('2) you can have your text scrambled for every letter but the first of each word.\n', 'green', 'on_cyan')
cprint('3) you can have your text scrambled for every letter of each word (a Big mess!)\n', 'green', 'on_cyan')
cprint('4) you can have the letter of your text randomly capitalized or lower-cased.\n', 'green', 'on_cyan')
cprint('ALL) if you want to see the effect of every previously mentioned function enter "ALL"\n', 'blue', 'on_yellow' )
# here the second possible choice is assigned a default value to make the subsequent loop work
choice_2 = 'xxxx'
# this loop produces the scrambled text according to the user's choice
while choice_2 not in second_choices:
    choice_2 = input('make your choice: ')
    if choice_2 == 'ALL':
        scrambled_text = '---------------------\n---------------------\n'
        scrambled_text += mid_scrambler(testo)
        scrambled_text += '\n---------------------\n---------------------\n'
        scrambled_text += but_first_scrambler(testo)
        scrambled_text += '\n---------------------\n---------------------\n'
        scrambled_text += total_scrambler(testo)
        scrambled_text += '\n---------------------\n---------------------\n'
        scrambled_text += rand_upper_lower(testo)
        scrambled_text += '\n---------------------\n---------------------\n'    
    elif choice_2 == '1':
        scrambled_text = mid_scrambler(testo)
    elif choice_2 == '2':
        scrambled_text = but_first_scrambler(testo)
    elif choice_2 == '3':
        scrambled_text = total_scrambler(testo)
    elif choice_2 == '4':
        scrambled_text = rand_upper_lower(testo)
    else:
        cprint("be carefull to type the write command! how'd you like your text to be scrambled?", "red")
# lastly the user can choose to save the scrambled text in a new .txt file, to have it printed in the console, or both
print ('\n\ndo you want your text printed in this console, saved in a file or both? (print/save/&)\n\n')
choice_3 = 'xxx'
while choice_3 not in third_choices:
    choice_3 =input('')
    if choice_3 in pt:
        cprint('Here is your scrambled text:\n', 'green')
        print(scrambled_text)
        cprint('Thanks for using Scrambler and the Scrambler testing environment, have a good day.', 'green')
        break
    elif choice_3 in sv:
        print('How do you want to name the file of your scrambled text? (write the name without the extension, it will be saved as a .txt file)\n' + warning_2)
        new_file_name = input('')
        while os.path.isfile(new_file_name + '.txt'):
            cprint('This file already exists! choose a new name!\n','red')
            new_file_name = input('')
        file = open(new_file_name + '.txt', 'w') 
        file.write(scrambled_text) 
        file.close()
    elif choice_3 == '&':
        print('How do you want to name the file of your scrambled text? (write the name without the extension, it will be saved as a .txt file)\n' + warning_2)
        new_file_name = input('')
        while os.path.isfile(new_file_name + '.txt'):
            cprint('This file already exists! choose a new name!\n','red')
            new_file_name = input('')
        file = open(new_file_name + '.txt', 'w') 
        file.write(scrambled_text) 
        file.close()
        cprint('Here is your scrambled text:\n', 'green')
        print(scrambled_text)
        cprint('Thanks for using Scrambler and the Scrambler testing environment, have a good day.', 'green')
    else :
        cprint('please tell me what to do(print/save/& (print and save)) and check the spelling!','red')
        
        


        
        

        


    






