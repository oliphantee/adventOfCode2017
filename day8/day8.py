f=open("day8.txt")

curMax=0
allVals={}
for line in f.readlines():
    line=line.rstrip().split()
    if line[4] not in allVals:
        allVals[line[4]]=0
    if eval("allVals[line[4]]"+line[5]+line[6]):
        if line[0] not in allVals:
            allVals[line[0]]=0
        if line[1]=="dec":
            allVals[line[0]]-=int(line[2])
        else:
            allVals[line[0]]+=int(line[2])
        if allVals[line[0]]>curMax:
            curMax=allVals[line[0]]
f.close()

print(max(allVals.values())) # part 1
print(curMax) # part 2