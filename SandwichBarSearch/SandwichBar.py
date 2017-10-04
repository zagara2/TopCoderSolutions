'''
Created on Mar 8, 2016

@author: Mickey
'''
def whichOrder(available, orders):
    available = set(available)
    orders = [set(x.split()) for x in orders]
    pos = 0
    while pos < len(orders):
        order = orders[pos]
        if order.issubset(available):
            return pos
        else:
            pos = pos + 1
        
    return -1 

