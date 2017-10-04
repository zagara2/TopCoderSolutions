'''
Created on Feb 25, 2016

@author: Mickey
'''
def decrypt(library,message):
    message_list = message.split()
    blankstr = ""
    posmessage = 0
    poslibrary = 0
    while True:
        entry = library[poslibrary]
        word = message_list[posmessage]
        if word == entry[2:]:
            blankstr = blankstr + entry[0]
            if posmessage + 1 < len(message_list):
                posmessage = posmessage + 1
                poslibrary = 0
                continue #go back to top of loop
        else:
            if poslibrary + 1 < len(library):
                poslibrary = poslibrary + 1
                continue
            
        if poslibrary + 1 == len(library) and word != entry[2:]: #if you are at the last lib entry and the word still doesn't match
            blankstr = blankstr + "?"
            poslibrary = 0
            if posmessage + 1 < len(message_list):
                posmessage = posmessage + 1
                continue
        if posmessage + 1 == len (message_list):
            break
    return blankstr
            
print decrypt(['N ---.-', 'I --.', 'L ..-..--.', 'W -', 'W .-----.', 'S .-.---.-.', 'X -.-.-.-.', 'W ---.-..--', 'S .-.----.', 'E ..'],"-.... -")
            

    