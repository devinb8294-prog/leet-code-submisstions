class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #2 pointer? One looking at curret index, one checking if the next index is the same
        #If so, replace last index

        l,r = 1,1
        while r <= len(nums)-1:
            if nums[r] > nums[r-1]:
                nums[l] = nums[r]
                l+=1
            r+= 1

        return l
                
                