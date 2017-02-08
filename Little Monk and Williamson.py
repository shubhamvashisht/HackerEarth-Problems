record=[]
nqueries=input()
for i in range(int(nqueries)):
    inputformat=[]
    inputformat=input().split()
    if inputformat[0]=="Push":
            record.append(int(inputformat[1]))
    elif inputformat[0]=="Diff":
        if len(record)==0:
            print(-1)
        else:
            maxi=max(record)
            mini=min(record)
            diff=maxi-mini
            print(diff)
            if maxi==mini:
                record.pop(record.index(maxi))
            else:
                maxin=record.index(maxi)
                minin=record.index(mini)
                record.pop(maxin)
                record.pop(minin)
    elif inputformat[0]=="CountHigh":
        if len(record)==0:
            print(-1)
        else:
            maxhigh=max(record)
            print(record.count(maxhigh))
    elif inputformat[0]=="CountLow":
        if len(record)==0:
            print(-1)
        else:
            minilow=min(record)
            print(record.count(minilow))
