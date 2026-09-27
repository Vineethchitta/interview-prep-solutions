class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        pot = n-1
        while i>=0:
            if nums[i+1] > nums[i]:
                while nums[pot] <= nums[i]:
                    pot-=1
                nums[i], nums[pot] = nums[pot], nums[i]
                print(nums)
                if (i+2)<n and (nums[i+1] >= nums[i+2]):
                    nums[i+1:n] = nums[n-1:i:-1]
                break
            elif nums[i] < nums[pot]:
                pot = i
            i-=1
        if i==-1:
            nums[0:n] = nums[n-1::-1]