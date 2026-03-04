from collections import defaultdict
def Grp_anagram(str):
    d=defaultdict(list)

    for i in str:
        key = tuple(sorted(i))
        d[key].append(i)

    return list(d.values())

str = input().split()
print(Grp_anagram(str))
           
    