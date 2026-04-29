class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        temp = []

        for num, count in counts.items():
            temp.append([count, num])
        temp.sort()

        res = []
        while len(res) < k:
            res.append(temp.pop()[1])
        return res



        