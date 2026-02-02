class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_cost = nums[0]
        sorted_nums = nums[1:]
        sorted_nums.sort()

        return first_cost + sorted_nums[0] + sorted_nums[1]
        