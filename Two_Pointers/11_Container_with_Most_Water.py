def maxArea(self, height: List[int]) -> int:
    L, R = 0, len(height)-1
    maxWater = 0 

    while L < R:
        smallerHeight = min(height[L], height[R])
        currWater = smallerHeight * (R-L)
        maxWater = max(maxWater, currWater)

        if height[L] < height[R]:
            L += 1

            while height[L] < smallerHeight:
                L += 1 
        
        else:
            R -= 1

            while height[R] < smallerHeight:
                R -= 1

    return maxWater