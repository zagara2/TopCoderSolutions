'''
Created on Mar 29, 2016

@author: Mickey
'''
def countVisible(trophies):
    blanklist = []
    countleft = 1
    maxleft = trophies[0]
    for item in trophies:
        if item > maxleft:
            countleft = countleft + 1
            maxleft = item
    blanklist.append(countleft)
    countright = 1
    trophies.reverse()
    maxright = trophies[0]
    for item in trophies:
        if item > maxright:
            countright = countright + 1
            maxright = item
    blanklist.append(countright)
    return blanklist

#print countVisible([1,4,2,5,3,7,1])