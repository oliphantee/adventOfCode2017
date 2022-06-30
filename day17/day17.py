inp=355
YEAR=2017
MAXVAL=50000000
curArray=[0]
curPos=0

while len(curArray)<=YEAR:
    curPos=(curPos+inp)%len(curArray)
    curArray=curArray[:curPos+1]+[len(curArray)]+curArray[curPos+1:]
    curPos+=1

curArray=curArray[curPos:]+curArray[:curPos]
print(curArray[1]) # part 1

curAfterZero=0
curLen=1
curPos=0
while curLen<MAXVAL:
    curPos=(curPos+inp)%(curLen)+1 # the +1 ensures nothing gets added before 0, so that 0 is always at index 0
    if curPos==1:
        curAfterZero=curLen
    curLen+=1
print(curAfterZero) # part 2

# I used a brute force solution for part 2 that didn't store the array, bypassing memory issues
# I'm curious if there's a way to use modular arithmetic to solve this
# That would probably be much faster, but I don't see how to do it
# Another method would be to figure out how to count down instead of up
# But I'm not sure how to track the current position in that case