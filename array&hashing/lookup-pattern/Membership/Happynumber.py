class Solution(object):
    def isHappy(self, n):
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            
            # Calculate sum of squares of digits
            # n = sum(int(digit) ** 2 for digit in str(n))
            
            total = 0
            for digit in str(n):
                total += int(digit) ** 2

            n = total
        return True
    
a1 = Solution()
print(a1.isHappy(19))