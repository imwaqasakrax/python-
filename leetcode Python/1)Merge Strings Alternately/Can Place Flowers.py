class Solution(object):
   def canPlaceFlowers(self , flowerbed, n):
    count = 0
    i = 0
    length = len(flowerbed)

    while i < length:
        if flowerbed[i] == 0:
            if (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        i += 1

    return False
