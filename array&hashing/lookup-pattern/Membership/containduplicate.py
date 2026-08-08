class Dplct:
    def contain_duplicate(self,nums):
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    
a1 = Dplct()
print(a1.contain_duplicate([1, 2, 1]))