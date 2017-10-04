'''
Created on Feb 25, 2016

@author: Mickey
'''
def getMinimum(s, oCost, xCost): 
    half_s_len = len(s)/2
    shalf1 = s[:half_s_len]
    shalf2 = s[half_s_len:]
    shalf1 = shalf1[::-1] #flips it
    #print shalf1
    if s.count("?") == 0:
        if shalf1 != shalf2:
            return -1
    total = 0
    new_shalf1flip = ""
    new_shalf2 = ""
    for x in range(len(shalf1)):
        if shalf1[x] == "?":
            if shalf2[x] == "o":
                total = total + oCost
                new_shalf1flip = new_shalf1flip + "o"
            if shalf2[x] == "x":
                total = total + xCost
                new_shalf1flip = new_shalf1flip + "x"
            if shalf2[x] == "?":
                if oCost < xCost:
                    total = total + oCost
                    new_shalf1flip = new_shalf1flip + "o"
                if xCost < oCost:
                    total = total + xCost
                    new_shalf1flip = new_shalf1flip + "x"
                if xCost == oCost:
                    total = total +oCost
                    new_shalf1flip = new_shalf1flip + "o" #defaults to o if costs are equal
        else:
            new_shalf1flip = new_shalf1flip + shalf1[x]
    for x in range(len(shalf2)):
        if shalf2[x] == "?":
            if shalf1[x] == "o":
                total = total + oCost
                new_shalf2 = new_shalf2 + "o"
            if shalf1[x] == "x":
                total = total + xCost
                new_shalf2 = new_shalf2 + "x"
            if shalf1[x] == "?":
                if oCost < xCost:
                    total = total + oCost
                    new_shalf2 = new_shalf2 + "o"
                if xCost < oCost:
                    total = total + xCost
                    new_shalf2 = new_shalf2 + "x"
                if xCost == oCost:
                    total = total +oCost
                    new_shalf2 = new_shalf2 + "o" 
        else:
            new_shalf2 = new_shalf2 + shalf2[x]
    #print new_shalf1flip
    #print new_shalf2
    if new_shalf1flip != new_shalf2:
        return -1
    return total 


            
    