import math as mt

f=open("day2.txt")

checkSum=0
sum2=0
for line in f.readlines():
    line=list(map(int,line.rstrip().split()))
    minNum=mt.inf
    maxNum=0
    for num in line:
        if int(num)<minNum:
            minNum=int(num)
        if int(num)>maxNum:
            maxNum=int(num)
    checkSum+=maxNum-minNum
    done=False
    for i in range(len(line)-1):
        if not done:
            for j in range(i+1,len(line)):
                if line[i]%line[j]==0:
                    sum2+=line[i]/line[j]
                    done=True
                    break
                if line[j]%line[i]==0:
                    sum2+=line[j]/line[i]
                    done=True
                    break
f.close()

print(checkSum)
print(sum2)