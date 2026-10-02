class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        prev_map = {}  # val : index

#        for i, n in enumerate(nums):
       #     diff = target - n
        #    if diff in prev_map:
        #        return [prev_map[diff], i]
        #    prev_map[n] = i