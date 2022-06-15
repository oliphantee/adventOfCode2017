f=open("day11.txt")

loc=[0,0]
maxDist=0
for dir in f.readline().rstrip().split(","): # there is probably a better way to handle hex grids, but this works and was easy to implement
    if dir=="n":
        loc[0]+=1
    elif dir=="s":
        loc[0]-=1
    elif dir=="ne":
        loc[1]+=1
    elif dir=="sw":
        loc[1]-=1
    elif dir=="nw":
        loc[0]+=1
        loc[1]-=1
    elif dir=="se":
        loc[0]-=1
        loc[1]+=1
    if loc[0] * loc[1] > 0:
        if abs(loc[0]+loc[1])>maxDist:
            maxDist=abs(loc[0]+loc[1])
    else:
        if abs(loc[0])>maxDist:
            maxDist=abs(loc[0])
        elif abs(loc[1])>maxDist:
            maxDist=abs(loc[1])

print(loc)
if loc[0]*loc[1]>0:
    print(abs(loc[0]+loc[1]))
else:
    loc=[abs(i) for i in loc]
    print(max(loc))

print(maxDist)
f.close()