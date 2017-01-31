num,places=input().split()
num=list(num)
places=int(places)
i=0
while i<places:
    if num[i]!='9':
        num[i]='9'
    else:
        places+=1
    i+=1
for j in num:
    print(j,end='')