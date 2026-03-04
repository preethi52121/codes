class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        str =list(s)
        l,r =0,len(str)-1
        while l<r:
            if str[l] not in vowels:
                l+=1
            elif str[r] not in vowels:
                r-=1
            else:
                str[l],str[r]=str[r],str[l]
                l+=1
                r-=1
        return "".join(str)


