def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==1:
       
        raw_input('Okay, this is the last loop, exp is 1, base is '+ str(base))
        return(base)
    else:
        raw_input('So,now recursing, exp is '+str(exp)+', base is '+ str(base))
        return(base*recurPower(base,exp-1))