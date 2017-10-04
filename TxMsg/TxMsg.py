'''
Created on Feb 11, 2016

@author: Mickey
'''
# returns true if let is a vowel, 
# otherwise returns false
def isVowel(let):
    return let in "aeiouAEIOU"

# returns true if all letter are vowels
# otherwise returns false
def allVowels(word): 
    for ch in word:
        if not isVowel(ch):
            return False
    return True 

# focus on transforming one word    
def transform(word):
    if allVowels(word):
        return word
    else:
        blankstring = ""
        for x in range(len(word)):
            if isVowel(word[x]) == False:
                if x == 0:
                    blankstring = blankstring + word[x]
                else:
                    if isVowel(word[x-1]):
                        blankstring = blankstring + word[x]
                
        return blankstring  
def getMessage(original):
    ret = ""
    for word in original.split():
        ret = ret + " " + transform(word)
    return ret.strip()

