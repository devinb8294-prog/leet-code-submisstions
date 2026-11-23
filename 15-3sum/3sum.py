class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #start from beginning
        #Sort nums
        #index i 
        #j - i +1
        #k len(nums) - 1
        #calculate sum of ojk == 0
        #Too low, increment j
        #Too high, increment k

        sums = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                
                elif total > 0:
                    k -= 1
                
                else:
                    sums.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j+= 1
            
        return sums
        
        
