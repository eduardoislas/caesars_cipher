# -*- coding: utf-8 -*-
"""
Created on Sat May 21 10:33:19 2022

@author: Eduardo Islas
"""
import sys

# Get only one argument from the command line, otherwise terminate the program with a status code of 1.
if (len(sys.argv) != 2):
    print("**ERROR: Only one non-negative integer parameter is needed**")
    exit(1)

# Get and save the argument (k = number of moves)
k = int(sys.argv[1])

# Prompt the user for the word to be encrypted
plaintext = list(input("plaintext: "))

# Alphabets, upper and lower case
upper_case_alphabet = range(ord('A'), ord('Z')+1)
lower_case_alphabet = range(ord('a'), ord('z')+1)
ciphertext = []

for character in plaintext:
    char_value = ord(character)
    rotated_value = char_value + k
    
    if char_value in upper_case_alphabet:
        while True:
            if rotated_value > upper_case_alphabet[-1]:
                rotated_value-=26
            else:
                ciphertext.append(chr(rotated_value))
                break
    elif char_value in lower_case_alphabet:
        while True:
            if rotated_value > lower_case_alphabet[-1]:
                rotated_value-=26
            else:
                ciphertext.append(chr(rotated_value))
                break
    else:
        ciphertext.append(character)
        continue

# Transform output
output = "".join(ciphertext)
print(f'ciphertext: {output} \n')
