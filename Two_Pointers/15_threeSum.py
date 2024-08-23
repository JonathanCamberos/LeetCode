def threeSum_1(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res


def threeSum_2(self, nums: List[int]) -> List[List[int]]:
    p, n, z = [], [], []
    res = set()

    for i in nums:
        if i < 0:
            n.append(i)
        elif i > 0:
            p.append(i)
        else:
            z.append(i)

    # sets for access
    P, N = set(p), set(n)

    # 1. (0, num, -num) if at least one 0
    if len(z) > 0:
        for i in P:
            n_target = -i
            if n_target in N:
                res.add((n_target, 0, i ))

    # 2. (0, 0, 0) if at least three 0's
    if len(z) > 2:
        res.add((0, 0, 0))

    # 3. (-, -, +) negative pairs
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            p_target = -(n[i] + n[j])
            if p_target in P:
                res.add(tuple(sorted([n[i], n[j], p_target])))
    
    # 4. (-, +, +) positive pairs
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            n_target = -(p[i] + p[j])
            if n_target in N:
                res.add(tuple(sorted([p[i], p[j], n_target])))

    return res	