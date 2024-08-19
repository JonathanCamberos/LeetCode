def containsDuplicate(self, nums: List[int]) -> bool:
    # hashmap
    seen = {}
    # for every element, check if element count >= 1
    for num in nums:
        if num in seen and seen[num] >= 1:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False