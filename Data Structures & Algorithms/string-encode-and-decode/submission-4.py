class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for string in strs:
            parts.append(str(len(string)))
            parts.append("#")
            parts.append(string)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        length = len(s)
        i = 0
        while i < length:
            l_str = ""
            while s[i] != '#' and s[i].isnumeric():
                l_str += s[i]
                i += 1
            from_index = i+1
            l_curr = int(l_str)
            to_index = from_index+int(l_str)
            string = s[from_index:to_index]
            decoded_strings.append(string)
            i = to_index
        return decoded_strings
            
        
            

            

