n=input()
listofn=list(map(int,input().split()))
a,b,c=0,0,0
for i in range(int(n)):
	if(i%3==0):
		a+=listofn[i]
	elif(i%3==1):
		b+=listofn[i]
	else:
		c+=listofn[i]
print(a,b,c)