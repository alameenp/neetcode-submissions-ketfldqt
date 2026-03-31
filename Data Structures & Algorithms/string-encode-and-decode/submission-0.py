class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word))+'#'+word
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i=0
        output = []
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            start = j+1
            string = s[start:start+length]
            output.append(string)
            i = start+length
        return output


                