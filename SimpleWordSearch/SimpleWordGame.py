'''
Created on Mar 8, 2016

@author: Mickey
'''
def points(player, dictionary):
    blanklist = []
    for word in player:
        if word in dictionary:
            blanklist.append(word)
    uniquewords = set(blanklist)
    sumcount = 0
    for item in uniquewords:
        thesquare = len(item)**2
        sumcount = sumcount + thesquare
    return sumcount
            
