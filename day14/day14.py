import random
from functools import reduce
import queue as q

keyString="xlqgujun"+"-"

size=128

def getKnotHash(inStr):
    length = 256
    array = list(range(length))
    curPos = 0
    skipSize = 0
    extraLengths = [17, 31, 73, 47, 23]
    lengths = list(map(ord, inStr)) + extraLengths

    for _ in range(64):
        for num in lengths:
            if curPos + int(num) < len(array):
                array = array[:curPos] + array[curPos:curPos + int(num)][::-1] + array[curPos + int(num):]
            else:
                revPortion = array[curPos:] + array[:(curPos + int(num)) % len(array)]
                revPortion = revPortion[::-1]
                array = revPortion[len(array) - curPos:] + array[(curPos + int(num)) % len(array):curPos] + revPortion[:len(array) - curPos]
            curPos = (curPos + int(num) + skipSize) % len(array)
            skipSize += 1
    sparseHash = array
    denseHash = []
    for i in range(16):
        denseHash.append(reduce(lambda x, y: x ^ y, sparseHash[i * 16:i * 16 + 16]))  # courtesy of https://www.geeksforgeeks.org/python-list-xor/

    finalAnswer = ""
    for i in denseHash:
        if len(hex(i)) == 3:
            finalAnswer += str(0) + str(hex(i)[2:])
        else:
            finalAnswer += str(hex(i)[2:])
    return finalAnswer

tot=0
grid=[]
oneLocs=[]
for row in range(size):
    curRow=str(bin(int(getKnotHash(keyString+str(row)), 16)))[2:].zfill(128)
    for i in range(len(curRow)):
        if curRow[i]=="1":
            oneLocs.append((row,i))
            tot+=1
    grid+=[list(curRow)]

print(tot) # part 1

numRegions=0
curLocs=q.Queue()
while len(oneLocs)!=0: # I'm not sure if this is the best method, but it is functional and on a fairly small size
    if curLocs.empty():
        numRegions+=1
        curLocs.put(oneLocs[0]) # get a new 1 that isn't part of a previous group
    else:
        curLoc=curLocs.get()
        if curLoc in oneLocs: # this means it's part of the current group, so we remove it and add its neighbors to the current group
            oneLocs.remove(curLoc)
            curLocs.put((curLoc[0]+1,curLoc[1])) # add all neighbors
            curLocs.put((curLoc[0]-1,curLoc[1]))
            curLocs.put((curLoc[0],curLoc[1]+1))
            curLocs.put((curLoc[0],curLoc[1]-1))

print(numRegions) # part 2