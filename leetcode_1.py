class Solution(object):
    def twoSum(nums, target):
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return
    
print(Solution.twoSum([1,3,5,7,9], 8))