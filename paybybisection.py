balance = 5317591
annualInterestRate = 0.00

monthlyRate = annualInterestRate/12.0
upperBound  = (balance* (1+monthlyRate) **12 /12.0)
lowerBound  = balance/12.00
payGuess    = (upperBound+lowerBound)/2
remainingBalance=0

def calcByGuess(opsGuess,opsBalance):
    # 'ops' means "operations' , just to avoid confusing myself :)
    for foo in [1,2,3,4,5,6,7,8,9,10,11,12]:
        opsBalance = opsBalance - opsGuess
        opsBalance = opsBalance + (monthlyRate * opsBalance)
        if (opsBalance<=0):
            break
    return(opsBalance)        


# so, a dirty endless loop... That's not right!    
while True:

    remainingBalance=calcByGuess(payGuess,balance)

    if abs(remainingBalance)<0.1:
        break
    elif remainingBalance<0:
       upperBound = payGuess
       payGuess   = round((upperBound+lowerBound)/2,2)
    else:
       lowerBound = payGuess
       payGuess   = round((upperBound+lowerBound)/2,2)


print("Lowest Payment: "+str(payGuess))