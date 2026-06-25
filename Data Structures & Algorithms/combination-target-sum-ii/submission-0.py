class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # 1. Sort candidates to group duplicates together
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # 2. Skip duplicate elements to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                # 3. Pass 'i + 1' instead of 'i' so an element cannot be reused
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result