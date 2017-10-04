'''
Created on Feb 9, 2016

@author: Mickey
'''
def decode(cipher, shift):
    the_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_string = ""
    if shift == 0:
        return cipher
    for chara in cipher:
        first_instance = the_alphabet.find(chara)
        new_index = first_instance - shift
        new_char = the_alphabet[new_index]
        final_string = final_string + new_char
    return final_string

