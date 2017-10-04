'''
Created on Feb 9, 2016

@author: Mickey
'''
def maxPoints(toss) :
    max_score = 0
    for x in toss:
        num_occur = toss.count(x)
        score = x * num_occur
        if score > max_score:
            max_score = score
    return max_score

