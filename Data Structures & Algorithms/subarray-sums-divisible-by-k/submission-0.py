class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Keep track of the prefix and initialize a hash map with the key->remainder and the value -> count. 
        prefix_sum = 0
        res = 0
        prefix_count = defaultdict(int)
        #Initialize with key -> value | 0 -> 1 for single-number list edge case 
        prefix_count[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k
            
            if remain in prefix_count:
                res += prefix_count[remain]
            prefix_count[remain] += 1
        return res