class Solution:
    def two_sum(self,nums,target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement],i]
            
            seen[nums[i]] = i
    
a1 = Solution()
print(a1.two_sum([1,2,3,5],target =8))