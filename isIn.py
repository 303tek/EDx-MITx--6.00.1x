def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Checked OK by EDx grader
    if aStr!='':
        midPoint=len(aStr)/2
        midChar=aStr[midPoint]
    
        if midChar==char:
            #we're done!
            return(True)
    
        else:    
                
            if char<midChar:
                return(isIn(char,aStr[:midPoint]))
    
            else:
                return(isIn(char,aStr[midPoint+1:]))
    else:
        return(False)                