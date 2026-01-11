from collections import defaultdict

def topKElements(nums, k):
    seen = defaultdict(int)
    
    #use bucket sort
    buckets = [[] for _ in range(len(nums) + 1)]
    
    #count frequency of each number
    for n in nums:
        seen[n] += 1
        print(seen)
    
    #add numbers in their buckets based on frequency - higher index means higher frequency
    for i, n in seen.items():
        buckets[n].append(i)
        
    print(buckets)
    
    #add highest freq numbers in result list
    result=[]

    #go backward in the bucket array
    for i in range(len(buckets)-1, 0, -1):
        for n in buckets[i]:
            result.append(n)
            if len(result) == k:
                return result

nums = [1,1,1,2,2,3,3,5,5,6,8,2,9,1,8,3,1,3,1,2,4,4,4,4,4,4,4]
k = 2


x = topKElements(nums, k)
print(x)