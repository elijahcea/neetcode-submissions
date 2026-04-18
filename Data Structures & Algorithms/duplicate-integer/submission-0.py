class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = []
        for n in nums:
            if newArr.count(n):
                return True
            else:
                newArr.append(n)
        return False
        