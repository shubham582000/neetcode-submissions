class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        res = []
        for key, val in freq.items():
            res.append([val,key])
        res.sort()

        arr = []
        while len(arr) < k:
            arr.append(res.pop()[1])
        return arr
        