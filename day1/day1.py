f=open("day1.txt")

line=f.readline().rstrip()

count=0
count2=0
for i in range(len(line)):
    if line[i]==line[(i+1)%len(line)]:
        count+=int(line[i])
    if line[i]==line[(i+len(line)//2)%len(line)]:
        count2+=int(line[i])

print(count) # part 1
print(count2) # part 2