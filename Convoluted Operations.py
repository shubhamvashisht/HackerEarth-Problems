numberOfOperation=int(input())
operation=[]
stack=[]
fatak=[]
spopindex=[None]*numberOfOperation
spushindex=[None]*numberOfOperation
npop=0
npush=0
for i in range(numberOfOperation):
    count=0
    operation=list(map(int,input().split()))
    if operation[0]==0:
        spopindex[i]=stack[-1]
        stack.pop(-1)
        npop+=1
    elif len(operation)==2:
        spushindex[i]=operation[1]
        stack.append(operation[1])
        npush+=1
    elif len(operation)==3:
        fatak=stack.copy()
        K=operation[1]
        X=operation[2]
        for j in range(i-1,K-1,-1):
            if spopindex[j]!=None:
                fatak.append(spopindex[j])
            if spushindex[j]!=None:
                fatak.pop(j-1)
        for l in range(len(fatak)):
            if fatak[l]<int(X):
                count+=1
        print(count)
