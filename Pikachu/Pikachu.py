'''
Created on Feb 24, 2016

@author: Mickey
'''
def check(word):
    word = word.lower()
    pos = 0
    while True:
        if word[pos:pos+2] == "pi":
            pos = pos + 2
            continue
        elif word[pos:pos+2] == "ka":
            pos = pos + 2
            continue
        elif word[pos:pos+3] == "chu":
            pos = pos +3
            continue
        else:
            break
    if pos >= len(word):
        return "YES"
    else:
        return "NO"

