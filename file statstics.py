import os
import sys
 
fname=sys.stdin.readline().split('\n')
fname=fname[0]
 
num_lines = 0
num_words = 0
num_chars = 0
 
with open(fname, 'r') as f:
	for line in f:
		words = line.split()
		num_lines += 1
		num_words += len(words)
		num_chars += len(line)
 
print num_lines
print num_words
print num_chars
 
fileattr=os.stat(fname)
 
print fileattr.st_uid
print fileattr.st_gid
print int(fileattr.st_ctime)