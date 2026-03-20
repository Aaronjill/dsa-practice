#Problem 3 — 🧠 DS&A
#Target: 18–20 min
#Given a list of fruit weights, find all pairs that sum to exactly a target weight. Return as a list of tuples. No duplicate pairs.

def find_pairs(list,target):
    
    sorted_list=sorted(list)
    l=0
    r=len(sorted_list)-1
    pairs=[]
    seen=set()
 
    while l<r:
        sum = sorted_list[l] + sorted_list[r]
        if sum == target:
            pair=(sorted_list[l],sorted_list[r])
            if pair not in seen:
                pairs.append(pair)
                seen.add(pair) 
            r-=1
            l+=1
        elif sum > target:
            r-=1
        else:
            l+=1
    return pairs

print(find_pairs([120, 80, 200, 150, 50, 100], target=200))
# → [(120, 80), (150, 50), (100, 100)? 
# wait — is (100,100) valid here? decide yourself
# → [(120, 80), (150, 50)]