from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups  = defaultdict(list)
        for i in strs:
            word = sorted(i)
            groups["".join(word)].append(i)
        return list(groups.values())
        