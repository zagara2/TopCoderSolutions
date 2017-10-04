'''
Created on Jan 31, 2016

@author: Mickey
'''
def minutesNeeded (numCakes, capacity):
    """
      return integer representing time to cook pancakes
      based on integer parameters as described below
      """
    floatcakes = float(numCakes)
    floatcapacity = float(capacity)
    floatdivresult = floatcakes/floatcapacity
    if floatdivresult == int(floatdivresult):#remember to try (float).is_integer()if problems arise 
        finalmins = (numCakes/capacity)*10 
    else:
        finalmins = (numCakes/capacity)*10 + 5
    number_dec = str(floatdivresult-int(floatdivresult))[1:]
    number_dec = float(number_dec)
    if number_dec > 0.5:
        finalmins = finalmins + 5
    return finalmins
    
    
                            