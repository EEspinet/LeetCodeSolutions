class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        output = ''
        for words in s:
            output = output + ' ' + words[::-1]
        return output.strip()
