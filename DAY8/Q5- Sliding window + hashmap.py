#Topic: Sliding window + hashmap — Stage 3 combination
#Target: 20–25 min
#Your pipeline receives a stream of fruit labels. Find the minimum window size that contains at least one of each required label.



def min_window_contains(labels,required):
    required_temp = required.copy()
    l=0
    r=1
    window=[]
    while len(required_temp) >0  and r+1 <len(labels):
        for n in range(l,r+1):
            if labels[n] in required_temp:
                required_temp.remove(labels[n])
                print(labels[n])
            window.append(labels[n])
            r+=1    
        #print(required_temp,len(required_temp))


    return window

labels  = ["apple","mango","apple","banana","mango","kiwi"]
required = ["mango", "banana"]

print(min_window_contains(labels, required))
# Find smallest window containing both mango AND banana
# → 3  (window "mango","apple","banana" at index 1-3)