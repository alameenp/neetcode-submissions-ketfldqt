class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        for word in strs:
            character_list = [0]*26
            for char in word:
                character_list[ord(char)-ord('a')] += 1
            key = tuple(character_list)
            if key not in group_dict:
                group_dict[key] = []
            group_dict[key].append(word)
        return list(group_dict.values())
        
        


        