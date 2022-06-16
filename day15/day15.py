aPrev=591
bPrev=393
aFactor=16807
bFactor=48271
aMod=4
bMod=8
magicMod=2147483647

numPairs=5000000#40000000 # use the bigger number for part 1

count=0

twoToThe16=2**16

for _ in range(numPairs):
    while True:
        aPrev=aPrev*aFactor%magicMod
        if aPrev%aMod==0:# remove this line for part 1
            break
    while True:
        bPrev=bPrev*bFactor%magicMod
        if bPrev%bMod==0: # remove this line for part 1
            break
    if aPrev%twoToThe16==bPrev%twoToThe16:
        count+=1

print(count)