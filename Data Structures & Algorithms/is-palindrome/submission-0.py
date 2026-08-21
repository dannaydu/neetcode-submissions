class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # l at start, r at end
        
        while l < r:
            # Skip non-alphanumeric from left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric from right
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers inward
            l += 1
            r -= 1
        
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))