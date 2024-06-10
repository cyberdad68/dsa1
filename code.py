import heapq
from collections import defaultdict
def min_time(t,test_cases):
    ans=[]
    for i in t:
        n,k=test_cases[i][0]
        a=test_cases[i][1]
        b=test_cases[i][2]
        category_min_time=defaultdict(list)
        for j in range(n):
            category_min_time=[a[j]].append(b[j])
        if len(category_min_time)<k:
            ans.append(-1)
            continue
        min_times=[]
        for times in category_min_time.values():
            min_times.append(min(times))
        min_times.sort()
        ans.append(sum(min_times[:k]))
    return ans
t=int(input().strip())
test_cases=[]
for i in range(t):
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    test_cases.append(((n,k),a,b))
ans=min_time(t,test_cases)
for i in ans:
    print(i)
        
