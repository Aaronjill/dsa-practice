#Problem 5 — Challenge 💪
#Topic: Sliding window — max value tracking
#Target: 15–20 min
#Your inspection line tracks defect counts per frame. You want to find the maximum total defects seen in any window of k consecutive frames — to identify the most stressed period.
#Write a function max_defects_in_window(frames, k) that returns that maximum sum.
def max_defects_in_window(items,k):
	top_sum=0
	for i in range (len(items)-k+1):
		cur_sum= sum(items[i:i+k])
		if cur_sum > top_sum:
			top_sum= cur_sum
	return top_sum
print(max_defects_in_window([2, 1, 5, 1, 3, 2], k=3))
#Windows: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
# → 9

max_defects_in_window([4, 4, 4, 4], k=2)
# → 8
#This one has a more elegant solution than just re-summing each window. See if you can spot it.