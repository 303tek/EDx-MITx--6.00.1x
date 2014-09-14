def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr=='':
        return(0)
    else:
        return(lenRecur(aStr[0:-1])+1)