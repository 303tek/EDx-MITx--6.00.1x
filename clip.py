def clip(lo, x, hi):
    '''
   [m] Takes in three numbers and returns a value based on the value of x.
    this function is fucked up
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return max(min(x,lo),max(x,hi))    