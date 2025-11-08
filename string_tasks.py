# ======================================================
# Task 1: Longest Substring Without Repeating Characters
# ======================================================


############### solution 1 #################
class LongestSubstring:
    def longest_substring(self, s: str)->int:
        l = []
        m = []

        for c in s:
            if c not in l:
                l.append(c)
            else:
                k =len(l)
                m.append(k)
                j =l.index(c)
                l.append(c)
                l = l[j+1:]
        k =len(l)
        m.append(k)
        print(max(m))

# test:                
sol = LongestSubstring()
sol.longest_substring('ABCABCFKAB')


############### solution 2 #################

class LongestSubstring1:
    def longest_substring(self, s: str) -> int:
        last, left, best = {}, 0, 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return print(best)

# test:                
sol = LongestSubstring1()
sol.longest_substring('ABCABCFKAB')



   
# ==========================================================
# Task 2: Check Circular Sequence of Four Consecutive Ones   
# ==========================================================

############### solution 1 #################
class FourConsecutiveOnes:
    def four_one(self, nums):
        nums = 2*str(nums)
        l = 0
        for num in nums:
            if num =='1':
                l+=1
                if l==4:
                    print(True)
                    return
            else:
                l=0
        print(False)

sol = FourConsecutiveOnes()
sol.four_one(1010111)




############### solution 2 #################

class FourConsecutiveOnes1:
    def one_(self, nums):
        nums = str(nums)
        n= len(nums)
        l=0
    
        for i in range(2*n):
            if nums[i % n] == '1':
                l+=1
                if l == 4:
                    print(True)
                    return
            else:
                l=0
        print(False)


sol = FourConsecutiveOnes1()
sol.one_(1010111)






