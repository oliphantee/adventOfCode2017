from functools import reduce

f=open("day10.txt")

length=256
array=list(range(length))
curPos=0
skipSize=0
extraLengths=[17, 31, 73, 47, 23]
lengths=list(map(ord,f.readline().rstrip()))+extraLengths

for _ in range(64):
    for num in lengths:
        if curPos+int(num)<len(array):
            array=array[:curPos]+array[curPos:curPos+int(num)][::-1]+array[curPos+int(num):]
        else:
            revPortion=array[curPos:]+array[:(curPos+int(num))%len(array)]
            revPortion=revPortion[::-1]
            array=revPortion[len(array)-curPos:]+array[(curPos+int(num))%len(array):curPos]+revPortion[:len(array)-curPos]
        curPos=(curPos+int(num)+skipSize)%len(array)
        skipSize+=1
sparseHash=array
denseHash=[]
for i in range(16):
    denseHash.append(reduce(lambda x, y: x ^ y, sparseHash[i*16:i*16+16])) # courtesy of https://www.geeksforgeeks.org/python-list-xor/

finalAnswer=""
for i in denseHash:
    if len(hex(i))==3:
        finalAnswer+=str(0)+str(hex(i)[2:])
    else:
        finalAnswer += str(hex(i)[2:])
print(array[0]*array[1])
print(finalAnswer)

f.close()