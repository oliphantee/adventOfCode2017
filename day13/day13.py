# This problem could probably be solved with mod math (maybe the chinese remainder theorem?)
# However, it is small enough that a brute force solution works and is easier to understand
f=open("day13.txt")

severity=0
allScanners=[]
for line in f.readlines():
    line=list(map(int,line.rstrip().split(": ")))
    allScanners.append(line)
    if line[0]%((line[1]-1)*2)==0:
        severity+=line[0]*line[1]

f.close()

print(severity) # part 1

t=0
while True:
    works=True
    for scanner in allScanners:
        if (scanner[0] + t) % ((scanner[1] - 1) * 2) == 0:
            works=False
            break
    if works:
        print(t) # part 2
        break
    t+=1
