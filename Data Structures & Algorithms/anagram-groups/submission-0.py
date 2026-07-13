class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in anagram_map:
               anagram_map[key].append(strs[i])
            else:
                anagram_map[key] = [strs[i]]
        return list(anagram_map.values())