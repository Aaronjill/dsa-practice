#Problem 4 — ML-Systems Flavored ⚙️
#Topic: Running statistics — a production monitoring pattern
#Target: 12–15 min
#Instead of storing all confidence scores and computing average at the end, your system needs a running average — updated one score at a time — because the stream never ends.
#Write a function running_average(scores) that returns a #list where each element is the average of all scores seen #so far up to that index.
def running_average (list):
		result=[]
		sum=0
		count=0
		for n in list:
			sum+=n
			count+=1
			avg= round((sum/count),2)
			result.append(avg)
		return result
		
		


print(running_average([0.9, 0.8, 0.7, 0.6]))
# → [0.9, 0.85, 0.8, 0.75]

running_average([1.0, 0.0, 1.0])
# → [1.0, 0.5, 0.67]  ← rounded to 2 decimal places