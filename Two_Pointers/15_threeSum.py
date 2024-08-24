def threeSum_1(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    # (index, value) iterator
    for i, a in enumerate(nums):
        
        # we are freezing one pointer on a negative number
        # if we hit postive number we can end
        if a > 0:
            break

        # if we hit a repeated negative number, skip
        if i > 0 and a == nums[i-1]:
            continue

        # mini twoSum problem
        # chunk of array to the right of the frozen negative number
        L, R, = i + 1, len(nums)-1
        while L < R:
            curr3Sum = a + nums[L] + nums[R]

            if curr3Sum < 0:
                L += 1
            elif curr3Sum > 0:
                R -= 1
            else:
                res.append([a, nums[L], nums[R]])

                # why dont we just shift over L?
                # following while loops moves L until we hit a new number
                # but we know that a + L + R --> 0
                # thus, there is no a + new_L + R != 0
                # so we must shift both pointers
                L += 1
                R -= 1

                while nums[L] == nums[L-1] and L < R:
                    L += 1

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