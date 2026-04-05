#Problem 4 — ML-Systems Flavored ⚙️
#Topic: Batch processing
#Target: 12–15 min
#Your CV model processes fruit images one by one, but the GPU is most efficient when processing in batches of size batch_size.
#Write a function create_batches(items, batch_size) that splits a list into batches. The last batch may be smaller if items don't divide evenly.
def create_batches(list,batch_size):
	batches =[]
	for i in range (0, len(list), batch_size):
		batches.append(list[i:i+batch_size])
	return batches 
print(create_batches([1,2,3,4,5,6,7], 3))
# → [[1,2,3], [4,5,6], [7]]

print(create_batches(["apple","mango","banana","kiwi"], 2))
# → [["apple","mango"], ["banana","kiwi"]]