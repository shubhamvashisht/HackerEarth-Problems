import itertools
finallis=[]
tcases=int(raw_input())
for i in range(tcases):
	rng=int(raw_input())
	arry=list(itertools.combinations(range(1,rng+1),2))
	for j in range(len(arry)):
		pair=arry[j]
		if pair[0]^pair[1]<=rng:
			finallis.append(pair)
	print len(finallis)
	del finallis[:]