def dletter(c):
    maxo=255
    first=67
    priasco=[67,71,73,79,83,89,97,101, 103, 107, 109, 113]
    for i in range(len(priasco)):
        if abs(priasco[i]-c)<maxo:
            maxo=abs(priasco[i]-c)
            first=priasco[i]
    return first

def dstr(s):
    mstr=""
    for i in range(len(s)):
        newchr=dletter(ord(s[i]))
        mstr=mstr+chr(newchr)
    return mstr

if __name__=='__main__':
    tcases=int(input())
    for i in range(tcases):
        nhh=input()
        print(dstr(input()))