f=open("day6.txt")

memBanks=[]
for val in f.readline().rstrip().split():
    memBanks.append(int(val))

seenBefore={}
count=0
while tuple(memBanks) not in seenBefore:
    seenBefore[tuple(memBanks)]=count
    blocks=max(memBanks)
    i=memBanks.index(blocks)
    memBanks[i]=0
    while blocks>0:
        blocks-=1
        i=(i+1)%len(memBanks)
        memBanks[i]+=1
    count+=1

print(count) # part 1
print(count-seenBefore[tuple(memBanks)]) # part 2