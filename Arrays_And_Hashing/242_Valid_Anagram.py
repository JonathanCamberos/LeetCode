def isAnagram_1(self, s: str, t: str) -> bool:
    # hashmap
    count = defaultdict(int)
    for x in s:
        count[x] += 1
    for x in t:
        count[x] -= 1
    for value in count.values():
        if value != 0:
            return False
    return True

def isAnagram_2(self, s: str, t: str) -> bool:
    # hashmap (as an array)
    count = [0] * 26
    for x in s:
        count[ord(x) - ord('a')] += 1
    for x in t:
        count[ord(x) - ord('a')] -= 1
    for value in count:
        if value != 0:
            return False
    return True