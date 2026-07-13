class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # Automatically creates a list for any new key accessed
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a tuple key
            key = "".join(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())