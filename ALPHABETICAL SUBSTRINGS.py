s = 'ababcdeefghijklm'
# I know, a little crude, but proud!
cBuffer=''
cCandidates=[]
lastChar=s[0]
for curChar in (s):
    if (curChar>=lastChar):
        cBuffer=cBuffer+curChar
    else:
        cCandidates+=[cBuffer]
        cBuffer=curChar
    lastChar=curChar        
#add last buffer
cCandidates+=[cBuffer]
print('Longest substring in alphabetical order is: '+max(cCandidates,key=len))