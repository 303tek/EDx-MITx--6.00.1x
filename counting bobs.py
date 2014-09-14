# counting bobs
s = 'graffibobobobbobirfbobob bob'
nPosition=0
doLoop=True
numBobs=0
while(doLoop):
    nPosition=s.find('bob',nPosition)
    if (nPosition!=-1):
        numBobs+=1
        nPosition+=1
    else:
        doLoop=False

print("Number of times bob occurs is: "+str(numBobs))