f = open("/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/queries.txt", 'r')

est_index_scan_cost = []
act_index_scan_cost = []
cards = []


for line in f:
	est_index_scan_cost.append(float(line.split("cost=")[1].split(" ")[0].split("..")[1]))
	act_index_scan_cost.append(float(line.split("time=")[1].split(" ")[0].split("..")[1]))
	cards.append(float(line.split("rows=")[2].split(" ")[0]))

print("--------est_index_scan_cost----------------")
for elem in est_index_scan_cost:
	print(elem)
print("------------------------")
print("--------act_index_scan_cost----------------")
for elem in act_index_scan_cost:
	print(elem)
print("------------------------")
print("------------cards-----------")
for elem in cards:
	print(elem)