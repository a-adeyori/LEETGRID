class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        is_true=0
       
        for i in range(len(flowerbed)-1):
            if i >0 and flowerbed[i]!=1:
                if flowerbed[i]!= 1 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    is_true+=1
            elif i==0 and flowerbed[i]== 0 and flowerbed[i+1]!=1:
                flowerbed[i]=1
                is_true+=1

        for i in range(len(flowerbed)):
            if i == len(flowerbed)-1 and flowerbed[i]!= 1  :
                if flowerbed[i-1]!=1:
                    is_true+=1

        return is_true >= n

        
            