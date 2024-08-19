def longestConsecutive(self, nums: List[int]) -> int: 
    numSet = set(nums)
    longest = 0
    for i in numSet:
        # found start of a sequence (left most element)
        if (i - 1) not in numSet: 
            currLen = 1
            while (i + currLen) in numSet:
                currLen += 1 
            longest = max(longest, currLen)

    return longest   