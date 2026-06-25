class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):       # base case: full-length arrangement
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:                  # skip elements already in the path
                    continue
                used[i] = True               # choose
                path.append(nums[i])
                backtrack(path, used)        # recurse
                path.pop()                   # un-choose
                used[i] = False              # un-choose the "used" flag too

        backtrack([], [False] * len(nums))
        return result