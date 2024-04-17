import string
import os
import sys

def Usage():
    if len(sys.argv) != 2 or len(sys.argv) < 2:
        print("[+] Usage: python3 php-non-alpha-encoder.py <alpha_string_to_encode>")
        sys.exit()

def check_alphabetic_chars(string):
    for char in string:
        if not char.isalpha():
            return False
    return True


non_alphabetical_char = string.printable[62:].replace('"','').replace("'","").replace("`","")
alphabetica_char = string.ascii_letters 


def encode(argument_to_encode):
    result = ""
    for i in range(0,len(argument_to_encode)):
        ascii_number_of_char = ord(argument_to_encode[i])
        for x in range(0,len(non_alphabetical_char)):
            selected_non_alpha_char = ord(non_alphabetical_char[x])
            xoring_result =  ascii_number_of_char ^ selected_non_alpha_char
            if chr(xoring_result) not in alphabetica_char and chr(xoring_result) != "\\":
                result += f'("{chr(selected_non_alpha_char)}"^"{chr(xoring_result)}").'
                break
    print(result.strip(result[-1]))


Usage()
argument = sys.argv[1]
check = check_alphabetic_chars(argument)
if check:
    encode(str(argument))
else:
    print("please enter a alphabetical chars to encode")
    sys.exit
