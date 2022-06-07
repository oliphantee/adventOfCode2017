f=open("day5.txt")

allVals=[]
for line in f.readlines():
    allVals.append(int(line.rstrip()))

f.close()

count=0
i=0
while i>=0 and i<len(allVals): # to get the part 1 answer, just delete the if and keep the else
    if allVals[i]>2:
        allVals[i]-=1
        i+=allVals[i]+1
    else:
        allVals[i]+=1
        i+=allVals[i]-1
    count+=1

print(count)