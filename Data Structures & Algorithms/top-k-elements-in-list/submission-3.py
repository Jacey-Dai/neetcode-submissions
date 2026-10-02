class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1
            
        sorted_res = sorted(result.keys(), key = lambda x:result[x], reverse = True)
        return sorted_res[:k]