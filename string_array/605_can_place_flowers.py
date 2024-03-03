"""
605. Can Place Flowers

Easy

You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
and 1 means not empty, and an integer n, return true if n new flowers can be 
planted in the flowerbed without violating the no-adjacent-flowers rule and 
false otherwise.
"""

def canPlaceFlowers(flowerbed, n):
    cur = 0
    available = 0
    while cur < len(flowerbed):
        if flowerbed[cur] == 0:
            if (cur - 1) > 0 and (cur+1)<len(flowerbed):
                if flowerbed[cur-1]==0 and flowerbed[cur+1]==0:
                    flowerbed[cur]=1
                    available+=1
            if cur-1<0 and cur+1<len(flowerbed):
                if flowerbed[cur+1] ==0:
                    flowerbed[cur]=1
                    available+=1
            if cur-1>0 and cur+1==len(flowerbed):
                if flowerbed[cur-1]==0:
                    flowerbed[cur]=1
                    available+=1                
        cur+=1
    return available==n

    

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    print(canPlaceFlowers(flowerbed, n)) # -> True