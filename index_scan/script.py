f = open("/home/dsladmin/Documents/vishal/index_scan/term_log.txt", 'r')
for line in f:
	if "cost=" in line:
		cost = line.split("cost=")[1].split(" ")[0].split("..")[1]
		print cost
	
