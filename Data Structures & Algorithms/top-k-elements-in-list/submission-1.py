class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through bucket sort
        count = {}

        # all elements CAN be 0-6 so make a array of 7
        # count = {1: 1, 2: 2, 3: 3}
        freq = [[] for i in range(len(nums) + 1)]

        # increment the count by one 
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # sort them into buckets
        # freq = [[], [1], [2], [3], [], [], []]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # go through each in reverse order
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res