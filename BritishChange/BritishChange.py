'''
Created on Feb 10, 2016

@author: Mickey
'''
def coins(pence):
    num_pounds = pence/240
    remainder_1 = pence%240
    num_shillings = remainder_1/12
    penniesleftover = remainder_1%12
    final_list = [num_pounds, num_shillings, penniesleftover]
    return final_list
    
