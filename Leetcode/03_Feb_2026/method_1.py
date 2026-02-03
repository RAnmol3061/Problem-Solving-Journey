class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        first = nums[0]
        p = 0
        q = 0

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                pass
            else:
                p = i
                break
        
        if p == 0:
            return False # As there is no way to form a segment when first element is bigger than second element

        for i in range(p, len(nums)-1):
            if nums[i] > nums[i+1]:
                pass
            else:
                q = i
                break
        print(q)
        
        for i in range(q,len(nums)-1):
            if nums[i] < nums[i+1]:
                pass
            else:
                return False
        return True
        