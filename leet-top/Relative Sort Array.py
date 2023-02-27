from collections import Counter 
from itertools import chain 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        prefix = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                prefix.append(arr1[i])
                
        dictt = Counter(arr1)
        suffix = []
        for i in range(len(arr2)):
            suffix.append([arr2[i]] * dictt[arr2[i]])
        return list(chain(*suffix)) + sorted(prefix)

        
        