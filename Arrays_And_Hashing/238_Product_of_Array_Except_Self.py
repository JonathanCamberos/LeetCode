def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    # create result array 
    res = [1] * (len(nums))

    # prefix for nth is product of (0 ... (n-1))
    for i in range(1, len(nums)):
        prefix = res[i-1] * nums[i-1]  # prefix of curr num  = (previous prefix * nums[i-1])
        res[i] = prefix                # set prefix for curr num

    # need holder as array is not set to 1
    postfix = 1 # postfix of next num

    # postfix for nth is product of (n+1 .... (len(nums)-1))
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * postfix     # set postfix for curr num
        postfix = nums[i] * postfix   # postfix of next num
    return res