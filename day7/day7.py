import statistics as st

f=open("day7.txt")

allRoots=set()
allChildren=set()
tree={}

for line in f.readlines():
    line=line.rstrip().split()
    root=line[0]
    val=int(line[1][1:-1])
    children=[child.rstrip(",") for child in line[3:]]
    tree[root]=(val,children)
    allRoots.add(root)
    for child in children:
        allChildren.add(child)

curNode=None
for root in allRoots:
    if root not in allChildren:
        print(root) # part 1
        curNode=root
        break

prevSibling=0

def getWeight(parent): # after finding the weight once I store it, memoization!
    weight=0
    if len(tree[parent])==3:
        val,children,weight=tree[parent]
        return weight
    val,children=tree[parent]
    for child in children:
        weight+=getWeight(child)
    weight+=val
    tree[parent]=(val,children,weight)
    return weight

while len(tree[curNode][1])!=0: # this feels messy, probably can be significantly cleaner
    allWeights=[getWeight(child) for child in tree[curNode][1]] # this lets us figure out if one child is different
    curSibling=st.mode(allWeights)
    isBalanced=True
    for child in tree[curNode][1]:
        if getWeight(child)!=curSibling:
            curNode=child
            isBalanced=False
            break
    if isBalanced: # if all the children are the same, then we should change this node
        print(prevSibling-getWeight(curNode)+tree[curNode][0]) # part 2
        break
    prevSibling=curSibling

print(prevSibling-getWeight(curNode)+tree[curNode][0]) # I think this is needed if the difference is in the leaves