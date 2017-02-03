t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	arr=[0 for i in range(1000001)]
	ct=0
	for s in range(n):
		a,b=map(int,raw_input().split(' '))
 
		if a==b:
			pass
		else:
			arr[a]+=1
			if arr[b]==0:
				ct+=1
			else:
				arr[b]-=1
	print ct