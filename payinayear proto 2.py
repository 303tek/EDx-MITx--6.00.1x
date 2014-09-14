balance = 3926
annualInterestRate = 0.2
# zOMG! This was hard!
monthlyRate=annualInterestRate/12.0
payGuess = 0

def calcByGuess(opsGuess,opsBalance):
    # 'ops' means "operations' , just to avoid confusing myself :)
    for foo in [1,2,3,4,5,6,7,8,9,10,11,12]:
        opsBalance = opsBalance - opsGuess
        opsBalance = opsBalance + (monthlyRate * opsBalance)
        if (opsBalance<=0):
            break
    return(opsBalance)        
        
while (calcByGuess(payGuess,balance)>0):
    payGuess = payGuess+10

print("Lowest Payment: " + str(payGuess))
        