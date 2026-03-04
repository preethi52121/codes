def Missing(nums):
    
    n= len(nums)
    
    exp= set(range(n+1))
    miss= exp - set(nums)

    return list(miss)


nums=list(map(int,input().split()))
print(Missing(nums))