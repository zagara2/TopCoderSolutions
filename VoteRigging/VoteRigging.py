'''
Created on Mar 29, 2016

@author: Mickey
'''
def firstBiggest(lst):
    if len(lst) == 1:
        return True
    for item in lst[1:]:
        if item >= lst[0]:
            return False
    return True   
    
def minimumVotes(votes):
    if firstBiggest(votes) == True:
        return 0
    changecount = 0
    while firstBiggest(votes)== False:
        listslice = votes[1:]
        maxi = max(listslice)
        max_index = listslice.index(maxi)
        votes[max_index+1] = votes[max_index+1] - 1
        votes[0] = votes[0] + 1
        changecount = changecount + 1
    return changecount

#print minimumVotes([5, 10, 7, 3, 8])