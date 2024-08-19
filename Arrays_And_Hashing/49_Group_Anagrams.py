def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
    
    # hashmap (sorted_string, [unsorted_string])
    groups = defaultdict(list)
    
    # add string via sorted word key
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    
    return groups.values()

def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap (count, [str])
        groups = defaultdict(list)
        
        for word in strs:
            
            # array for char count
            count = 26*[0]

            # unicode of char         
            for ch in word:  
                count[ord(ch)-ord('a')] += 1
            
            # matches tuples to group 
            groups[tuple(count)].append(word)
            
        return groups.values()