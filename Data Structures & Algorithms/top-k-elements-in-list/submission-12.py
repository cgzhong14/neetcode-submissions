class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]  # index = frequency
        for num, req in count.items():
            buckets[req].append(num)
        
        res = []
        for freq in range(len(buckets) - 1, 0, -1):    # highest frequency first
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res