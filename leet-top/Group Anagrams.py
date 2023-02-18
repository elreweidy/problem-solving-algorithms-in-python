from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagram_groups[key].append(word) 

        groups = []
        for key in anagram_groups:
            groups.append(anagram_groups[key])
        
        return groups
        