class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # Step 3: Place each number into its frequency bucket
        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
        # Step 4: Traverse buckets from high frequency to low
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        count = {}









        


                
      











    