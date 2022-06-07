import itertools as iter

f=open("day4.txt")

def getAnagrams(string):
    anagrams=[]
    for anagram in iter.permutations(string):
        if "".join(anagram) not in anagrams: # this forces identical letters to be treated as identical, preventing repeats
            anagrams.append("".join(anagram))
    return anagrams


count=0
count2=0
for line in f.readlines():
    line=line.rstrip().split()
    isPassword=True
    isPassword2=True
    for word in line: # the part 2 code is fairly slow, not sure if there is a more optimal way
        if line.count(word)>1:
            isPassword=False
        matches=0
        for anagram in getAnagrams(word):
            if anagram in line:
                matches+=line.count(anagram)
        if matches>1:
            isPassword2=False
    if isPassword:
        count+=1
    if isPassword2:
        count2+=1
f.close()

print(count)
print(count2)
