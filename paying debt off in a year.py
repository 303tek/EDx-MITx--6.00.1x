balance = 4773
annualInterestRate = 0.2
## #
totalPaid=0
## Init this to zero!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
payGuess=300
monthlyRate=annualInterestRate/12.0
opsBalance=balance
while True:
    ## Ok , init the fucking values
    opsBalance=balance
    totalPaid=0
    ## Add 10 bucks, if is the first loop, will be 10 :)
    payGuess  = payGuess  + 10

    for i in [1,2,3,4,5,6,7,8,9,10,11,12]:

        
        opsBalance = opsBalance  - payGuess
        opsBalance = opsBalance  + (monthlyRate * opsBalance)
        
        print('Loop        :'+str(i))
        print('opsBalance  :'+str(opsBalance))
        print('payGuess    :'+str(payGuess))
        # raw_input('** PAUSED **')

        if opsBalance <=0 :
            ## No need to continue, exit the FOR loop
            break
         
    print('*******Out of FOR - payGuess*12: '+str(payGuess*12))

    if (payGuess*12)>=balance:
        break
                
print("Lowest Payment: " + str(payGuess))