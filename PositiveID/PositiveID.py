'''
Created on Apr 18, 2016

@author: Mickey
'''
#import itertools 
#from itertools import chain, combinations


'''
def allIn(lst, string):
    string = string.split(",")
    for item in lst:
        if item not in string:
            return False
    return True
 '''   

def allIn2(lst1, lst2):
    for x in lst1:
        if x not in lst2:
            return False
    return True
    

'''
def compare(lst, biglist):
    max = 0
    for item in lst:
        l1 = item
        cc = [z for z in lst if z != item]
        current = [l1]
        for thing in cc:
            current.append(thing)
            count = 0
            for item in biglist:
                if allIn(current, item):
                    count += 1
            if count > 1:
                max = len(current)
    return max
    '''

def compare2(lst, biglist):
    max = 0
    for thing in combs(lst):
        count  = 0
        for item in biglist:
            itemlst = item.split(",")
            if allIn2(thing, itemlst):
                count += 1
        if count > 1:
            max = len(thing)
    return max
    


def combs(x):
    return sum([map(list, combinations(x, i)) for i in range(len(x) + 1)], [])

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def all_same(items):
    return all(x == items[0] for x in items)


        

def maximumFacts2(suspects):
    mydict = {}
    for item in suspects:
        traitlist = item.split(",")
        for trait in traitlist:
            if trait not in mydict:
                mydict[trait] = 1
            else:
                mydict[trait] += 1
    mylist = [k for (k,v) in mydict.items() if v>1]
    #list2 = sorted([(v,k) for (k,v) in mydict.items()], reverse = True)
    y = compare2(mylist, suspects)
    #print combinations(mylist, len(mylist))
    #z = permute(mylist)
    #print z

    #print mylist
    #print list
    return y

def maximumFacts(suspects):
    maxmatches = 0
    thisguy = []
    thatguy = []
    for x in range(0, len(suspects)):
        thisguy = suspects[x].split(",")
        for y in range(x+1, len(suspects)):
            matches = 0
            thatguy = suspects[y].split(",")
            matches = len(set(thisguy) & set(thatguy))
            if matches > maxmatches:
                maxmatches = matches
    
    return maxmatches
'''
you want to make the least number of comparisons possible for an elegant and fast solution
'''

print maximumFacts(["big,tall,loud,happy,male,scarred,tattooed,dirty",
"short,male,beard,quiet,happy,tanned,handsome",
"female,pretty,blond,quiet",
"somnambulistic",
"happy,tiny,stout,male,tanned,beard,blond"])