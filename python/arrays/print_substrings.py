def printSubstrings(string):
	for i in range(len(string)):
		ts = ""
		for j in range(i,len(string)):
			ts+=string[j]
			print(ts)


#main
string = input();
printSubstrings(string)
