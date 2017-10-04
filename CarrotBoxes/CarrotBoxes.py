'''
Created on Feb 25, 2016

@author: Mickey
'''
def theIndex(carrots,amount): 
    lastbox = 0
    while amount > 0:
        maxboxindex = carrots.index(max(carrots)) #index of box with the most carrots
        carrots[maxboxindex] = carrots[maxboxindex] - 1
        lastbox = maxboxindex #makes a note of what box she just ate from
        amount = amount -1 #how many carrots are left?
    return lastbox

#print theIndex([14,36,52,86,27,97,3,67], 300)