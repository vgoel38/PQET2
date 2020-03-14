f = open("sorted_plans.txt", 'r')

est_sort_cost = []
est_output_cost = []
act_sort_cost = []
act_output_cost = []


for line in f:
	est_scan_cost = float(line.split("cost=")[2].split(" ")[0].split("..")[1])
	est_sort_cost.append(float(line.split("cost=")[1].split("..")[0]) - est_scan_cost)
	est_output_cost.append(float(line.split("cost=")[1].split(" ")[0].split("..")[1]) - float(line.split("cost=")[1].split("..")[0]))

	act_scan_cost = float(line.split("time=")[2].split(" ")[0].split("..")[1])
	act_sort_cost.append(float(line.split("time=")[1].split("..")[0]) - act_scan_cost)
	act_output_cost.append(float(line.split("time=")[1].split(" ")[0].split("..")[1]) - float(line.split("time=")[1].split("..")[0]))

for elem in est_sort_cost:
	print(elem)
print("------------------------")
for elem in est_output_cost:
	print(elem)
print("------------------------")
for elem in act_sort_cost:
	print(elem)
print("------------------------")
for elem in act_output_cost:
	print(elem)
print("------------------------")
