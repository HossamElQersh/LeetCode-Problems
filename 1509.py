from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        res = float("inf")
        nums.sort()
        if len(nums) <= 4:
            return 0
        for l in range(4):
            r = len(nums) - 4 + l
            res = min(res, nums[r] - nums[l])
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.minDifference([1, 5, 0, 10, 14, 13, 41, 12, 32, 4]))
