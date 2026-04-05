#Problem 3 — DS&A Essential 🧠
#Topic: Two pointers (first introduction)
#Target: 15–18 min
#You have a sorted list of fruit weights in grams. You need to find if any two fruits together hit an exact target weight for a combo pack.
#Write a function find_combo_pair(weights, target) that returns a tuple of the two weights, or None if no pair exists.
def find_combo_pair(weights,target):
	l=0
	r=len(weights) -1
	while l < r:
		total = weights[l] + weights[r]
		if total == target:
			return (weights[l],weights[r])
		elif total > target:
			r -= 1
		else:
			l+=1
	return None 
print(find_combo_pair([120, 150, 200, 240, 300], 390) )# → (150, 240)
print(find_combo_pair([120, 150, 200, 240, 300], 500))  # → None
print(find_combo_pair([100, 200, 300], 300))         # → (100, 200)
#Hint if needed: think about using both ends of the list simultaneously.