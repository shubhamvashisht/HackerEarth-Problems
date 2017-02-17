tcases=int(raw_input())
for i in range(tcases):
	size=raw_input()
	array=map(int,raw_input().split())
	array.sort(reverse=True)
	for p in array:
		print p,
	print