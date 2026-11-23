class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #2 Pointer approach. If current num is val, replace it with next one i guess

        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] == val:
                left = nums[l]
                right = nums[r]
                nums[l] = right
                nums[r] = l

                r -= 1
            else:
                l += 1
        return l
            


        