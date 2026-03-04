def Rev_wrd(m):
    s = m[::-1]
    wrdss = s.split()
    return " ".join(wrdss[::-1])
wrdss=input()
print(Rev_wrd(wrdss))