class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "qprs", "8": "tuv", "9": "wxyz",
        }
        
        res = [""]
        for digit in digits:
            # Heavy C-level optimization bypassing manual Python loop overhead
            res = [curStr + c for curStr in res for c in digitToChar[digit]]
            
        return res