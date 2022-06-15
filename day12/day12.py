import queue as q

f=open("day12.txt")

allMappings={}
for line in f.readlines():
    line=line.rstrip().split(" <-> ")
    allMappings[line[0]]=line[1].split(", ")

f.close()

allChanged=q.Queue()
allUsed=set()
count=0

for i in allMappings.keys():
    if i not in allUsed:
        curGroup=set()
        allChanged.put(i)
        allUsed.add(i)
        while not allChanged.empty():
            curNum=allChanged.get()
            curGroup.add(curNum)
            for num in allMappings[curNum]:
                if num not in curGroup:
                    allChanged.put(num)
                    allUsed.add(num)
        if i=="0":
            print(len(curGroup)) # part 1
        count+=1

print(count) # part 2


f.close()