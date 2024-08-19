def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        
    # occurence hashmap 
    num_count = {}
    for key in nums:
        num_count[key] = 1 + num_count.get(key, 0)

    # list comprehension - create len() empty buckets 
    num_buckets = len(nums) + 1  # empty list requires at least 1 bucket
    freq_buckets = [[] for i in range(num_buckets)]

    # sort into buckets 
    for num, occurences in num_count.items():
        freq_buckets[occurences].append(num)

    res = []

    # decreasing for loop, starting by grabbing highest bucket
    for i in range(len(freq_buckets) - 1, 0, -1):
        
        # grabbing elements in curr bucket
        for num in freq_buckets[i]:
            res.append(num)
            
            # check if kth reached
            if len(res) == k:
                return res