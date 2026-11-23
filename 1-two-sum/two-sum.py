class Solution:
    def twoSum(self, nums: list[int], target: int):
        numMap = {}
        n = len(nums)

        #build hash table
        for i in range(n):
            numMap[nums[i]] = i
        
        #find complement
        for i in range(n):
            complement = target - nums[i]

            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        