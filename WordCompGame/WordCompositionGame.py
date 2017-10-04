'''
Created on Mar 23, 2016

@author: Mickey
'''

def score(listA,listB,listC):
    listA = set(listA)
    listB = set(listB)
    listC = set(listC)
    intofall = listA & listB & listC
    intAB = listA&listB
    intAC = listA&listC
    intBC = listB&listC
    AplusB = listA.union(listB)
    AplusC = listA.union(listC)
    BplusC = listB.union(listC)
    diffA = listA.difference(BplusC)
    diffB = listB.difference(AplusC)
    diffC = listC.difference(AplusB)
    ascore = 0
    bscore = 0
    cscore = 0
    for word in listA:
        if word in intofall:
            ascore = ascore + 1
        elif word in intAC and not word in intofall:
            ascore = ascore + 2
        elif word in intAB and not word in intofall:
            ascore = ascore + 2
        elif word in diffA:
            ascore = ascore + 3
    for word in listB:
        if word in intofall:
            bscore = bscore+1
        elif  word in intAB or word in intBC:
            bscore = bscore + 2
        elif word in diffB:
            bscore = bscore + 3
    for word in listC:
        if word in intofall:
            cscore = cscore + 1
        elif word in intAC or word in intBC:
            cscore = cscore + 2
        elif word in diffC:
            cscore = cscore + 3
    newstr = str(ascore)+"/"+str(bscore)+"/"+str(cscore)
    return newstr



#print score(["dog", "mouse"], ["dog", "pig"], ["dog", "cat"])
            