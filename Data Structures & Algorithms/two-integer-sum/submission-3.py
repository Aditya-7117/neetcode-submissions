class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(nums):
            answer = target - v 
            if answer in hashmap:
                return [hashmap[answer], i]
            else:
                hashmap[v] = i
        return