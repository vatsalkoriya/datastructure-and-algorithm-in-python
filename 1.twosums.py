class  solutions:
    def twoSums(self,nums,target):
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
             if nums[i] + nums[j] == target:
                return[i,j]
             else:
                return -1
s = solutions()
s1 = s.twoSums([1,2,3],3)
print(s1)