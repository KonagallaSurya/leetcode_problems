class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        substring=""  
        max_count=0
        count=0
        for i in range(k):
            substring+=s[i]
            if s[i] in 'aeiou':
                count+=1
        max_count=count
        for right in range(k,len(s)):
            substring+=s[right]
            if right>=k-1:
                if s[right] in 'aeiou':
                    count+=1
                if substring[0] in 'aeiou':
                    count-=1
                max_count=max(count,max_count)
                substring=substring[1:]
        return max_count
        