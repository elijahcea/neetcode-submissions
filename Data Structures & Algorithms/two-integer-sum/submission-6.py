class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for idx, n in enumerate(nums):
            indices[n] = idx

        for idx, n in enumerate(nums):
            diff = target - n

            if diff in indices and indices[diff] != idx:
                return [idx, indices[diff]]
                                
        return []
        