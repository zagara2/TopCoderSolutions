'''
Created on Mar 9, 2016

@author: Mickey
'''
def uniqueLetters(word):
    word_list = sorted(list(word))
    word_set = set(word_list)
    wordunique = sorted(list(word_set))
    if word_list == wordunique:
        return True
    else:
        return False
def maxLength(letters):
    answer = 1
    for templen in range(0, len(letters)):
        tempS = letters[templen:]
        if uniqueLetters(tempS) and len(tempS)> answer:
            answer = len(tempS)
        for templen2 in range(0, len(letters)):
            tempS2 = tempS[0:len(tempS)-templen2]
            if uniqueLetters(tempS2)and len(tempS2) > answer:
                answer = len(tempS2)
    return answer

print maxLength("thisisanaptbeforethedukemidterm")