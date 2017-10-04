'''
Created on Apr 5, 2016

@author: Mickey
'''
def reportDuplicates(names):
    freqdict = {}
    for item in names:
        if item not in freqdict:
            freqdict[item] = 1
        else:
            freqdict[item] += 1
    blanklist = []
    #print sorted(freqdict)
    for (k, v) in sorted(freqdict.items()):
        if v > 1:
            mystr = k + " "+ str(v)
            blanklist.append(mystr)
    return blanklist

print reportDuplicates(["A", "B", "A", "C", "A", "B", "A", "D", "D", "D"])    