class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move the left pointer rightward if it points to a non-alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            
            # Move the right pointer leftward if it points to a non-alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare the characters case-insensitively
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers inward for the next comparison
            l += 1
            r -= 1
            
        return True