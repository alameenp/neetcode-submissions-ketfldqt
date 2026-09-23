class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length_of_string = len(string)
            encoded_string += str(length_of_string)
            encoded_string +="#"
            encoded_string +=string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        length = len(s)
        i = 0
        print(s)
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
            
        
            

            

