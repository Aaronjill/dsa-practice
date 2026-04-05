#Topic: Dict aggregation
#Target: 10–12 min
#Your grading system processes fruits all day. At the end of the day you get a list of detection events like this:
def grade_count(events):
	result={}
	for d in events:
		
		if d["label"] not in result:
			result[d["label"]]={}
		
		result[d["label"]][d["grade"]] = result[d["label"]].get(d["grade"],0)+1
	return result 

events = [
    {"label": "apple",  "grade": "A"},
    {"label": "mango",  "grade": "B"},
    {"label": "apple",  "grade": "A"},
    {"label": "apple",  "grade": "B"},
    {"label": "mango",  "grade": "A"},
]
print(grade_count(events))
#Write a function grade_summary(events) that returns a dict showing how many of each grade each fruit got:
#{    "apple": {"A": 2, "B": 1},"mango": {"A": 1, "B": 1}}