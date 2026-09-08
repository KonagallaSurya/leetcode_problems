class Solution:
    def countCommas(self, n: int) -> int:
        c=999
        if n<=999:
            return 0
        else:
            return n-c
    