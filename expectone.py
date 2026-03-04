# if duplicates not needed
'''def Except_one(arr):
    
    seen= set()
    dup = set()
    for i in arr:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
    return list(dup)
arr=list(map(int,input().split()))
print(Except_one(arr))'''

# if duplicates needed

def Except_one(arr):
    
    dup = []
    for i in arr:
        if arr.count(i)>1:
            dup.append(i)
    return dup
arr=list(map(int,input().split()))
print(Except_one(arr))