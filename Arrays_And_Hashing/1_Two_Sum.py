def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    tracking = {}

    # for every index  
    for i in range (len(nums)):
                            
        complement = target - nums[i]

        # search for complement of curr element
        if complement in tracking and tracking[complement] != i:
            return [i, tracking[complement]]

        # if miss, push (currElement, index) into HashMap
        tracking[nums[i]] = i