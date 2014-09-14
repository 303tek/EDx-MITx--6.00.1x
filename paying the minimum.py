balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# ##
nPaid = 0;
for nCurrentMonth in [1,2,3,4,5,6,7,8,9,10,11,12]:
    print("Month: "+str(nCurrentMonth))
    print("Minimum monthly payment: " + str(round(monthlyPaymentRate*balance,2)))
    nPaid   = nPaid   + monthlyPaymentRate*balance
    balance = balance + (annualInterestRate/12.0)*balance
    balance = balance - (monthlyPaymentRate*balance)
    print("Remaining balance: " + str(round(balance,2)))
    
print("Total paid: " + str(round(nPaid,2)))    
print("Remaining balance: " + str(round(balance,2)))