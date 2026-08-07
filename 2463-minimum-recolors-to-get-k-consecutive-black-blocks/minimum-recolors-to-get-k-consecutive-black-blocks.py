class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        maxblack=0
        count=0
        left=0
        for right in range(len(blocks)):
            if blocks[right]=="B":
                count+=1
            if right>=k-1:
                maxblack=max(count,maxblack)
                if blocks[left]=="B":
                    count-=1
                left+=1
        return k-maxblack
