val=277678

curLoc=1
radius=1

while curLoc<val:
    radius+=2
    curLoc=radius**2

print(radius,curLoc)
curLoc-=(radius-1)/2 # this is the center of the bottom row now

while curLoc-(radius-1)/2>val:
    curLoc-=radius-1

print((radius-1)/2+abs(curLoc-val))

direction=(0,1)

