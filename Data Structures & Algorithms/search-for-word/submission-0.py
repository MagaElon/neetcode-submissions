class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            # 1. Success Base Case
            if i == len(word):
                return True
            
            # 2. Prune/Fail Base Cases
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i] or 
                (r, c) in visited):
                return False
            
            # 3. Mark the cell as visited
            visited.add((r, c))
            
            # 4. Explore all 4 adjacent directions
            # If any direction returns True, the whole path is valid
            found = (backtrack(r + 1, c, i + 1) or
                     backtrack(r - 1, c, i + 1) or
                     backtrack(r, c + 1, i + 1) or
                     backtrack(r, c - 1, i + 1))
            
            # 5. Backtrack: remove from visited
            visited.remove((r, c))
            
            return found

        # Since the word can start anywhere, try starting from every single cell
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
                    
        return False
    