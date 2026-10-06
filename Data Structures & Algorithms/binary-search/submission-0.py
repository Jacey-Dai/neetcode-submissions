class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid

            elif nums[mid] > target:
                right = mid
            
            else:
                return mid
        

