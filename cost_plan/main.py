import sys
import math

mr_cost = 0.0000436
nlj_cost = 0.00010179

sort1_cost = 0.000006829
sort0_cost = 0.000017643
extra1_cost = 0.000043152
extra0_cost = 0.0001649

smj_cost_1 = 0.0000996
# smj_cost_2 = 0.000185831
# smj_cost_2 = 0.000538381
smj_cost_2 = 0.0002192

cpu_op_cost = 0.0000776397001419
cpu_tup_cost = 0.0000691418225144
group_output_cost = 0.000298512 #found from the group_by_hash plan
cpu_avg_cost = 0.000126916

def materialisation_plus_rescan(inner_rel_card, loops):
	return mr_cost * inner_rel_card * loops

def nlj(outer_rel_card, inner_rel_card):
	materialisation_plus_rescan_cost = materialisation_plus_rescan(outer_rel_card-1, inner_rel_card)
	processing_cost = nlj_cost * outer_rel_card * inner_rel_card

	return materialisation_plus_rescan_cost, processing_cost

def sort_outer_rel(rel_card, correlation):
	sorting_cost = (correlation * sort1_cost + (1-correlation) * sort0_cost) * rel_card * math.log(rel_card,2)
	output_cost = (correlation * extra1_cost + (1-correlation) * extra0_cost) * rel_card

	return sorting_cost , output_cost

def sort_inner_rel(rel_card, correlation, join_card):
	sorting_cost = (correlation * sort1_cost + (1-correlation) * sort0_cost) * rel_card * math.log(rel_card,2)
	initial_output_cost = (correlation * extra1_cost + (1-correlation) * extra0_cost) * rel_card
	rescan_output_cost = extra1_cost * max(join_card-rel_card,0)

	return sorting_cost , initial_output_cost + rescan_output_cost

def smj(outer_rel_card, inner_rel_card, join_card):
	processing_cost_1 = smj_cost_1 * (outer_rel_card + inner_rel_card)
	processing_cost_2 = smj_cost_2 * join_card

	return processing_cost_1 , processing_cost_2

def group_by_sort(num_groups_cols, rel_card, num_groups):
	group_comparison_cost = cpu_op_cost * num_groups_cols * rel_card
	output_cost = cpu_tup_cost * num_groups
	return group_comparison_cost + output_cost

def group_by_hash(num_groups_cols, rel_card, num_groups):
	hashing_cost = hash_op_cost * rel_card
	group_comparison_cost = cpu_op_cost * num_groups_cols * rel_card
	output_cost = group_output_cost * num_groups
	return hashing_cost + group_comparison_cost, output_cost

def group_by_sort_and_agg(avg_cols, other_agg_cols, rel_card, num_groups_cols, num_groups):
	group_comparison_cost = cpu_op_cost * num_groups_cols * rel_card
	avg_cost = cpu_avg_cost * avg_cols * rel_card
	other_agg_cost = cpu_op_cost * other_agg_cols * rel_card
	output_cost = cpu_tup_cost * num_groups
	return group_comparison_cost + avg_cost + other_agg_cost + output_cost

def group_by_hash_and_agg(avg_cols, other_agg_cols, rel_card, num_groups_cols, num_groups):
	hashing_cost = cpu_op_cost * rel_card
	group_comparison_cost = cpu_op_cost * num_groups_cols * rel_card
	avg_cost = cpu_avg_cost * avg_cols * rel_card
	other_agg_cost = cpu_op_cost * other_agg_cols * rel_card
	output_cost = group_output_cost * num_groups
	return hashing_cost + group_comparison_cost + avg_cost + other_agg_cost, output_cost

if __name__ == "__main__":

	#print('smj = ' + str(smj(2609129,2525745,2609129)))
	#print('outer_sort = ' + str(sort_outer_rel(2609129, 0.454579)))
	#print('inner_sort = ' + str(sort_inner_rel(2528312, 0.998105, 2528312)))
	# print('mat = ' + str(materialisation_plus_rescan(2,2609129)))
	#print('nlj = ' + str(nlj(2609129,2)))
	#print('count = ' + str(agg_except_avg(36244344, 1, 4, 34512222)))
	#print('avg = ' + str(avg(36244344, 1, 4, 34512222)))
	#print('group_by_sort = ' + str(group_by_sort(3, 14835720, 14835720)))
	#print('group_by_hash = ' + str(group_by_hash(1, 36244344, 2331601)))
	print('group_by_sort_and_agg = ' + str(group_by_sort_and_agg(0, 1, 460456073, 1, 133)))
	#print('group_by_hash_and_agg = ' + str(group_by_hash_and_agg(1, 2,35143848, 3, 74496)))
