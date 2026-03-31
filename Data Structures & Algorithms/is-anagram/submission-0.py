class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_freq_dict = {}

        for letter in s:
            if letter in word_freq_dict:
                word_freq_dict[letter] += 1
            else:
                word_freq_dict[letter] = 1
        
        for letter in t:
            if letter in word_freq_dict:
                word_freq_dict[letter] -= 1
            else:
                word_freq_dict[letter] = -1
        for key in word_freq_dict:
            if word_freq_dict[key]  != 0:
                return False
        return True