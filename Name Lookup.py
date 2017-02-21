table={}
number_of_student=input()
for i in range(int(number_of_student)):
	roll_number,name=input().split()
	if int(roll_number)>1000000:
	    table[int(roll_number%1000000)]=name
	else:
	    table[roll_number]=name
queries=input()
for j in range(int(queries)):
	qroll=input()
	print(table.get(qroll))