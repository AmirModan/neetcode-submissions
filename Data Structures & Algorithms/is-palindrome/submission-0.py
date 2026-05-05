class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum()).lower()
        for i in range(int(len(clean_s) / 2)):
            if clean_s[i] != clean_s[-1-i]:
                return False
        return True