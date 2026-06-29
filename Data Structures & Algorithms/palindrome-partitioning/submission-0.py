class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        # O(1) Palindrome check thanks to caching (Memoization)
        
        def is_palindrome(start: int, end: int) -> bool:
            if start >= end:
                return True
            return s[start] == s[end] and is_palindrome(start + 1, end - 1)

        def backtrack(start, path):
            # Base Case: If we reached the end of the string, the path is valid!
            if start == len(s):
                result.append(path[:])
                return
            
            # Explore every possible cut from the 'start' index to the end
            for end in range(start, len(s)):
                # Use our efficient O(1) cache check
                if is_palindrome(start, end):
                    # Choose: slice the palindromic substring
                    path.append(s[start : end + 1])
                    # Recurse: move the start pointer past this slice
                    backtrack(end + 1, path)
                    # Un-choose: backtrack
                    path.pop()

        backtrack(0, [])
        return result                  

