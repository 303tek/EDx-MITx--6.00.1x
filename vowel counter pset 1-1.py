# vowel counter
s = 'azcbobobegghakl'

numVowels=0
for currentVowel in s:
    if currentVowel in 'aeiou':
        numVowels=numVowels+1
        
    


print('Number of vowels: '+str(numVowels))