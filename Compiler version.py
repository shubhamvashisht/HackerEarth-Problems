try:
	while True:
		line=raw_input()
		help1=line.split('//',1)[0]
		print help1.replace('->','.')+line[len(help1):]
except EOFError:
	done = True
except Exception as e:
	print e