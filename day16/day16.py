f=open("test.txt")

dancers=list("abcde")#list("abcdefghijklmnop")
LENGTH=5#16
NUMSTEPS=20

def spin(num):
    global dancers
    dancers=dancers[-num:]+dancers[:-num]

def exchange(i,j):
    global dancers
    temp=dancers[j]
    dancers[j]=dancers[i]
    dancers[i]=temp

def partner(a,b):
    global dancers
    exchange(dancers.index(a),dancers.index(b))

# so for part 2 you can actually ignore all the partner swaps
# this is because there are an even number of partner swaps and the partner swaps are completely independent of the other moves
# this means that every time through the same mappings occur (like 1->3, 2->1 and 3->2 for example)
# which means we could simplify this drastically by finding the mappings once and then running that 1 billion times
# but that is still gonna be pretty slow
# it's better to determine the loops within the mappings, then mod the 1 billion by the length of the loop
# which will get weird as not all loops need to be same length
pt2Cmds=[]
for cmd in f.readline().rstrip().split(","):
    if cmd[0]=="s":
        spin(int(cmd[1:]))
        pt2Cmds.append(("spin",int(cmd[1:])))
    else:
        cmd=cmd.split("/")
        if cmd[0][0]=="x":
            exchange(int(cmd[0][1:]),int(cmd[1]))
            pt2Cmds.append(("exchange",(int(cmd[0][1:]),int(cmd[1]))))
        else:
            partner(cmd[0][1:],cmd[1])

print("".join(dancers))

dancers=list(range(LENGTH))
for cmd in pt2Cmds:
    if cmd[0]=="spin":
        spin(cmd[1])
    else:
        exchange(cmd[1][0], cmd[1][1])


for j in range(0,NUMSTEPS+1,2):
    finalDancers=list(range(LENGTH))
    #print(dancers)
    for i in range(LENGTH):
        index=dancers[i]
        loopLen=1
        curLoop=["abcdefghijklmnop"[index]]
        while index!=i:
            index=dancers[index]
            loopLen+=1
            curLoop.append("abcdefghijklmnop"[index])
        finalDancers[i]=curLoop[(j-1)%loopLen]
        #print(curLoop,loopLen)

    print("".join(finalDancers))
    
f.close()