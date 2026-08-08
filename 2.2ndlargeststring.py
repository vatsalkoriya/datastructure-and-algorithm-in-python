class Solutions:
    def secondLargest(self,s):
        digits = set()

        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))

        if len(digits) < 2:
            return -1
        
        digits = sorted(digits)
        return digits[-2]
    
s = Solutions()
s1 = s.secondLargest("awdawd21254")
print(s1)