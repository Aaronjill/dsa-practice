#Problem 1 — Warm-up 🔥
#Topic: List comprehension + conditions
#Target: 5–8 min
#Your pipeline receives a batch of fruit weights. Return a new list that contains only weights between 100g and 300g (inclusive), each rounded to the nearest 10.

def filter_weights(weights):
	filtered = [round(w,-1) for w in weights if w <=300 and w >= 100]
	return filtered


print(filter_weights([95, 123.4, 250.7, 310, 180.1, 99.9]))
# → [120, 250, 180]