class Solution:
    def isFascinating(self, n: int) -> bool:
        a=2*n
        b=3*n
        out=str(n)+str(a)+str(b)
        if len(out)!=9:
            return False
        for i in range(1,10):
            if str(i) not in out:
                return False
        return True