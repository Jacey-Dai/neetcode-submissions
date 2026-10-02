class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1

        final  = sorted(result.keys(), key = lambda x: result[x], reverse = True)
        return final[:k]
            
        