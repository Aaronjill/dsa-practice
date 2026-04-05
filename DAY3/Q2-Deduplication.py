#Problem 2 — Data Handling 📦
#Topic: Deduplication — a new pattern
#Target: 10–12 min
#Your CV pipeline sometimes detects the same fruit twice #in consecutive frames (duplicate detections). You're given a list of detection IDs and you need to return a new list with duplicates removed, but original order preserved.


def remove_duplicates(ids):
	distinct_id = []
	for id in ids:
		if id not in distinct_id:
			distinct_id.append(id)
	return distinct_id
print(remove_duplicates([101, 203, 101, 305, 203, 406]))
# → [101, 203, 305, 406]

print(remove_duplicates([1, 1, 1, 2]))
# → [1, 2]
#⚠️ Constraint: Do not use set() directly on the list — that destroys order.