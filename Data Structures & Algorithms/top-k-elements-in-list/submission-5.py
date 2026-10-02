class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1
            
        sorted_res = sorted(result.keys(), key = lambda x:result.get(x), reverse = True)
        return sorted_res[:k]

from collections import Counter

#class Solution:
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # most_common(k) returns a list of (element, frequency) tuples
        # return [item[0] for item in count.most_common(k)]