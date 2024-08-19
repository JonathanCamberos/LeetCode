# example: "5#hello3#bye"
    
def encode(self, strs: List[str]):
    ans = "" 
    for word in strs:
        ans += str(len(word)) + "#" + word

    return ans

# decode above pattern
def decode(self, s: str):
    ans = []
    i = 0

    # complete until end of encoded string
    while i < len(s):
        j = i

        # find the #
        while s[j] != "#":
            j += 1
        
        # anything left will be int
        length = int(s[i:j])

        # point to start of string
        i = j + 1 

        # point to +1 after string (for substringing)
        j = i + length

        # grab string 
        ans.append(s[i:j])

        # start of next section
        i = j

    return ans