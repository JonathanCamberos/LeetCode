 def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l,r = 0,len(numbers)-1

    while l < r:
        tmp = numbers[l] + numbers[r]

        if tmp > target:
            r -= 1
        elif tmp < target:
            l += 1
        else:
            return [l+1,r+1]