class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, length = 0, len(flowerbed)
        
        while i < length and n>0:
            if flowerbed[i]==1:
                i += 2
            elif flowerbed[i]==0:
                if i+1==length:
                    n -= 1
                    i += 1
                elif flowerbed[i+1]==0:
                    n -= 1
                    i += 2
                else:
                    i += 3
        return n==0
                
                
        