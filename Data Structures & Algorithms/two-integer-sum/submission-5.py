class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, val in enumerate(nums):
            if val in complements:
                return([complements.get(val), i])
            complements[target-val] = i

            