#Problem 1 — Warm-up 🔥
#Topic: Data handling — multi-format string parsing
#Target: 5–8 min
#Your pipeline receives a messy batch log where each line has a different separator:
    
    
def parse_logs(logs):
        details=[]
        for f in logs:
             fruit,count,grade=f.split("|")
             dict={"fruit":fruit,"count":count,"grade":grade}
             details.append(dict)
                 
          
        return details
logs = [
    "apple|42|A",
    "mango|17|B",
    "banana|9|A"
]
print (parse_logs(logs))
#Write parse_logs(logs) that returns a list of dicts:
#[
#    {"fruit": "apple",  "count": 42, "grade": "A"},
#    {"fruit": "mango",  "count": 17, "grade": "B"},
#    {"fruit": "banana", "count": 9,  "grade": "A"}
#]