'''
Created on Mar 2, 2016

@author: Mickey
'''
def getMaximumSubset(words):
    return len(set(["".join(sorted(x)) for x in words]))