class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        print(res)
        for val in res.values():
            
            if val > 1:
                return True
        return False

        