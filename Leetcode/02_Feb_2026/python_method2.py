class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_cost = nums[0]
        loop = nums[1:]
            
        second_cost = float('inf')
        third_cost = float('inf')
        

        for i in loop:
            if i < second_cost:
                third_cost = second_cost 
                second_cost = i 
                
            elif i < third_cost:
                third_cost = i

        return first_cost + second_cost + third_cost
        