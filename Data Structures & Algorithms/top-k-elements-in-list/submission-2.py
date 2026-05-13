class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets where index = frequency
        # Each bucket stores numbers that appear that many times
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 3: Place each number into its frequency bucket
        for num, c in count.items():
            freq[c].append(num)

        # Step 4: Traverse buckets from high frequency to low
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                # Step 5: Stop once we collect k elements
                if len(res) == k:
                    return res  