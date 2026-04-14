import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = set(string.ascii_lowercase + 
                      string.ascii_uppercase +
                      string.digits)
        forward = ""
        backward = ""

        i = 0
        j = len(s) - 1
        while i < len(s):
            if s[i] in letters:
                forward += s[i]
            if s[j] in letters:
                backward += s[j]

            i += 1
            j -= 1
        
        forward = forward.lower()
        backward = backward.lower()

        return forward == backward

