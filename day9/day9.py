f=open("day9.txt")

i=0 # index
totScore=0 # final answer
curScore=0 # current depth
line=f.readline().rstrip()
f.close()
isGarbage=False # whether or not inside "<>"
totGarbage=0 # total number of characters inside "<>" that weren't cancelled

while i<len(line):
    c=line[i]
    if isGarbage:
        if c=="!":
            i+=2
        elif c==">":
            isGarbage=False
            i+=1
        else:
            totGarbage+=1
            i+=1
    else:
        if c=="{":
            curScore+=1
            i+=1
        elif c=="}":
            totScore+=curScore
            curScore-=1
            i+=1
        elif c=="!":
            i+=2
        elif c=="<":
            isGarbage=True
            i+=1
        elif c==">":
            isGarbage=False
            i+=1
        else:
            i+=1

print(totScore) # part 1 answer
print(totGarbage) # part 2 answer