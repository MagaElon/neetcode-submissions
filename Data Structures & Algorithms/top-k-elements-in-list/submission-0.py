class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Size is len(nums) + 1 because a number could appear up to len(nums) times
        freq = [[] for i in range(len(nums) + 1)]

        # 1. Count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Map frequency to list of numbers (Buckets)
        for n, c in count.items():
            freq[c].append(n)
        
        # 3. Collect top k results
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        