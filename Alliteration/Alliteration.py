'''
Created on Mar 8, 2016

@author: Mickey
'''
def countall(words):
    words = [x[0].lower() for x in words]
    if len(words) == 1:
        return 0
    pos = 0
    allit_count = 0
    allit = False 
    while pos < len(words):
            
        if words[pos] == words[pos+1]:
            allit = True
            pos = pos + 1
            if pos == len(words)-1:
                allit_count = allit_count + 1
                break
        else:
            if allit == True:
                allit = False
                allit_count = allit_count + 1
                pos = pos + 1
            else:
                pos = pos + 1
        if pos == len(words)-1:
                break
    return allit_count

print countall(["Round"])