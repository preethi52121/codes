def Print_one(arr):
    result = 0
    for i in arr:
        result ^= i
    return result
arr=list(map(int,input().split()))
print("output:",Print_one(arr))
        
