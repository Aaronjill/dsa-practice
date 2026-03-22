#Problem 5 — 💪 Challenge
#Target: 20–25 min
#Your grading line processes fruit in batches. Each batch has a priority level (1=highest, 3=lowest). You need to process batches in priority order, but batches arrive at different times.
#Given a list of (arrival_time, priority, batch_id) tuples, return the order in which batches should be processed — always picking the highest priority available batch at each step.

import heapq

def schedule_batches(batches):
    batches = sorted (batches,key=lambda x :x[0])
    priority = []
    hold=[]
    time=0
    i = 0
    while i < len(batches) or hold:
        while i<len(batches) and batches[i][0]<= time:
            t,p,batch=batches[i]
            heapq.heappush(hold,(p,batch))
            i+=1
        if hold:
            p,batch=heapq.heappop(hold)
            priority.append(batch)
            time+=1
        else:
            time=batches[i][0]
    return priority  
batches = [(0,2,"B1"), (0,1,"B2"), (1,3,"B3"), (2,1,"B4")]
print(schedule_batches(batches))
# At time 0: B1 and B2 available → pick B2 (priority 1)
# At time 1: B1, B3 available → pick B1 (priority 2)  
# At time 2: B3, B4 available → pick B4 (priority 1)
# Then: B3
# → ["B2", "B1", "B4", "B3"]
#```

#---

## 📝 For each problem tell me:
#1. Which pattern did I use?
#2. Comment plan (before code)
#3. Solution