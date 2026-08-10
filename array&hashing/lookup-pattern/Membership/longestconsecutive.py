class Solution:
    def longestConsecutive(self,nums):
        seen = set(nums)
        longest = 0

        for i in seen:
            if i - 1 not in seen:
                length = 1
            
                while i + length in seen:
                    length += 1
            longest = max(length,longest)
        
        return longest
    
a1 = Solution()
print(a1.longestConsecutive([1,2,2,3,4,9,5]))