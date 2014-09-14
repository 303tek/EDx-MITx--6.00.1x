def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here

    numCounter=1
    retTuple=()    
    for n in aTup:
        print(n)
        if numCounter%2!=0: # Odd
            retTuple+=(aTup[numCounter-1],)
        numCounter+=1    
    return(retTuple)            