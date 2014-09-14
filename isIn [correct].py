def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    minBound = 0
    maxBound = len(aStr)-1

    center = (maxBound + minBound)/2

    if (len(aStr)==0):
        return(False)

    elif (aStr[center] == char):
        return(True)


    elif (len(aStr) == 1):
        return(aStr == char)

    elif (aStr[center] == char):
        return(True)

    elif (char < aStr[center]):
        return(isIn(char, aStr[:center-1]))

    else:
        return(isIn(char, aStr[center+1:]))