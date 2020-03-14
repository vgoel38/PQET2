f = open("output.txt", 'r')

for line in f:

	total_act_run_cost = float(line.split("time=")[1].split(" ")[0].split("..")[1]) - float(line.split("time=")[1].split(" ")[0].split("..")[0])
	left_act_run_cost = float(line.split("time=")[2].split(" ")[0].split("..")[1]) - float(line.split("time=")[2].split(" ")[0].split("..")[0])
	right_act_run_cost = float(line.split("time=")[4].split(" ")[0].split("..")[1]) - float(line.split("time=")[4].split(" ")[0].split("..")[0])

	print(total_act_run_cost - left_act_run_cost - right_act_run_cost)