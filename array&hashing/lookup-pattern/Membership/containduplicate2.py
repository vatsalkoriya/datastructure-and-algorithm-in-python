class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        if i >= k:
            seen.remove(nums[i-k])
        return False
    
a1 = Solution()
print(a1.containsNearbyDuplicate([1,2,3,3],k=2))