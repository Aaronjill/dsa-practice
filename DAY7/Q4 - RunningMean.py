#Problem 4 — ⚙️ ML-Systems
##Target: 15–18 min
#Your monitoring system receives confidence scores in real time. 
#Flag any score that is more than 2 standard deviations below the running mean as an
#anomaly. Return list of flagged indices.

def detect_anomalies(scores):
    index=[]
    history=[]
    for i, score in enumerate(scores):
        if len(history) > 1:
            mean=sum(history)/len(history)
            var=sum((x-mean)**2 for x in history)/len(history)
            roll_sd=var**0.5
            threshold = mean-(2*roll_sd)
            if score < threshold:
                index.append(i)
        history.append(score)
    return index
            
scores = [0.9, 0.85, 0.88, 0.91, 0.87, 0.2, 0.86, 0.1]

print(detect_anomalies(scores))
# → [5, 7]
#You'll need running mean and running std. Think about what you know about running statistics.