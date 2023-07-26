from types import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = set(nums)

        i = 0
        for a in nums:
            neededB = target - a
            if (neededB in numsSet):
                b = nums.index(neededB)
                if (b != i):
                    return [i, b]
            i += 1
