'''
Created on Apr 5, 2016

@author: Mickey
'''
def whosDishonest(club1, club2, club3):
    club1 = set(club1)
    club2 = set(club2)
    club3 = set(club3)
    memberdict = {}
    for person in club1:
        if person not in memberdict:
            memberdict[person] = ["club1"]
    for person in club2:
        if person not in memberdict:
            memberdict[person] = ["club2"]
        else:
            memberdict[person].append("club2")
    for person in club3:
        if person not in memberdict:
            memberdict[person] = ["club3"]
        else:
            memberdict[person].append("club3")
    blanklist = []
    for (k, v) in sorted(memberdict.items()):
        if len(v)>1:
            blanklist.append(k)
    return blanklist

#print whosDishonest(["BOBBY"], ["BOB","BOBBY"], ["BOB"])