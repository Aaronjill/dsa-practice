#Problem 3 — DS&A Essential 🧠
#Topic: Hashmap fast lookup
#Target: 15–18 min
#Your grading system logs which conveyor belt each fruit #came from and its defect status. Given two separate lists — one of belt IDs and one of defect flags — return a dict mapping each belt ID to its defect rate (percentage of defective fruits, rounded to 1 decimal).


def defect_rate_by_belt(belt_ids,defective):
	rate={}
	for b_id , is_def in zip(belt_ids,defective):
		rate.setdefault(b_id,[ ]).append(is_def)
		
	return {b_id: round(sum(val)/len(val)*100,1)for b_id ,val in rate.items()}
	

		
		
		
		
belt_ids  = [1, 2, 1, 3, 2, 1, 3, 3]
defective = [0, 1, 1, 0, 1, 0, 1, 1]
print(defect_rate_by_belt(belt_ids, defective))
# → {1: 33.3, 2: 100.0, 3: 66.7}