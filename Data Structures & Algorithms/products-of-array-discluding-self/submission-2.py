import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right = []
        left = []
        curr = 1
        for val in nums:
            right.append(curr)
            curr = val*curr
        
        curr = 1
        for val in reversed(nums):
            left.append(curr)
            curr = val*curr
        left = reversed(left)
        return ([l*r for l,r in zip(left, right)])