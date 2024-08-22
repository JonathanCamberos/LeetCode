def threeSum(self, nums: List[int]) -> List[List[int]]:
    p, n, z = [], [], []
    res = set()

    for i in nums:
        if i < 0:
            n.append(i)
        elif i > 0:
            p.append(i)
        else:
            z.append(i)

    # sets for O(1) access
    P, N = set(p), set(n)

    # 1. (-, 0, +) complements if at least one 0
    if len(z) > 0:
        for i in range(len(p)):
            if -(p[i]) in N:
                res.add((-(p[i]), 0, p[i]))
    
    # 2. (0, 0, 0) group if at least three 0's
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
                res.add(tuple(sorted([n_target, p[i], p[j]])))

    return res