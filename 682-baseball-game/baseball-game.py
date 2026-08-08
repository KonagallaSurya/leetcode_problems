class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if i=='+':
                ans.append(ans[-1]+ans[-2])
            elif i=='D':
                a=ans[-1]
                ans.append(2*a)
            elif i=='C':
                ans.pop()
            else:
                ans.append(int(i))
        return sum(ans)