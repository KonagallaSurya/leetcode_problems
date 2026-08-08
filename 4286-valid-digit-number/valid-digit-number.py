class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        ns=str(n)
        xs=str(x)
        if xs in ns and ns[0] != xs:
            return True
        else:
            return False