# bisection search test
lowPoint=0
highPoint=100
myGuess=0
ans=''
print("Please think of a number between 0 and 100!")
while (ans!='c'): 
    myGuess=int((highPoint+lowPoint)/2)
    print("Is your secret number "+str(myGuess)+"?")
    ans=str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if ans.lower() not in "hlc": 
        print("Sorry, I did not understand your input.")
    else:
        if ans.lower()=='h':
            highPoint=myGuess
        elif ans.lower()=='l':
            lowPoint=myGuess
        elif ans.lower()=='c':
            break
print("Game over. Your secret number was: "+str(myGuess))