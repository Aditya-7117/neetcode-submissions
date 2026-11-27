class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # This sum is nothing but keeping the first number constant and doing 2 sum. 
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:#Handles duplicates. 
                continue

            #Start with Two Sum. 
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1 #Very important to handle the edge case of not repeating the same set 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res