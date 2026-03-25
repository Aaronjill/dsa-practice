#Your pipeline monitors per-label confidence scores in a sliding window of size K. 
#At each step, return the label with the lowest average confidence in the current window — the most at-risk label.
def at_risk_label(lists,k):
    
    info={}
    i=0
    track=[]
    t=0
    while i+k <= len(lists):
        for index in range(i,k+t):
            print (index)
            dict=lists[index]
            fruit=dict["label"]
            value=dict["confidence"]
            info.setdefault(fruit,[]).append(value)
        t+=1
#        info={key: sum(v for v in val)/len(val) for key,val in info.items()}
        for key,val in info.items():
            print(key,val)
            avg=sum(v for v in val)/len(val)
            info[key]=avg
        sort_info = sorted(info.items(),key=lambda item:item[1])
        info={}
        track.append(sort_info[0][0])      
        i+=1
    return track       
detections = [
    {"label": "apple",  "confidence": 0.9},
    {"label": "mango",  "confidence": 0.4},
    {"label": "apple",  "confidence": 0.8},
    {"label": "mango",  "confidence": 0.3},
    {"label": "banana", "confidence": 0.7},
    {"label": "apple",  "confidence": 0.2},
]
k = 3

print(at_risk_label(detections, k))
# → ["mango", "mango", "mango", "apple"]