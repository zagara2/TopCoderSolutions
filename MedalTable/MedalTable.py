'''
Created on Apr 18, 2016

@author: Mickey
'''
from operator import itemgetter   

def generate(results):
    mydict = {}
    for item in results:
        itemlist = item.split()
        gold = itemlist[0]
        silver = itemlist[1]
        bronze = itemlist[2]
        if gold not in mydict:
            mydict[gold] = [1, 0, 0]
        else:
            mydict[gold][0] += 1
        if silver not in mydict:
            mydict[silver] = [0, 1, 0]
        else:
            mydict[silver][1] +=1
        if bronze not in mydict:
            mydict[bronze] = [0, 0, 1]
        else:
            mydict[bronze][2] += 1
    mylist = mydict.items()
    tuple_list = [(k, v[0], v[1], v[2]) for (k, v) in mylist]
    tuple_list.sort(key = itemgetter(0)) #sort alphabetically
    tuple_list.sort(key = itemgetter(3), reverse = True) #sort by bronze
    tuple_list.sort(key = itemgetter(2), reverse = True) #sort by silver
    tuple_list.sort(key = itemgetter(1), reverse = True) #sort by gold
    #note to self: for some reason, if an elt in your tuple is a list,  you can't itemgetter
    #an index of the list (e.g. key = itemgetter(1)[1]). you just have to make a really big tuple?
    #and then access indices of the big tuple
    #is there a better way to do this? was I writing something weird?
    final = []
    for item in tuple_list:
        mystr = item[0] + " " + str(item[1]) + " " + str(item[2]) + " " + str(item[3])
        final.append(mystr.strip())
    return final

print generate(["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"])
        
    