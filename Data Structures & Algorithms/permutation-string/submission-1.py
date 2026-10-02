class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        count2 = {}
        for i in range(n1):
            char = s2[i]
            count2[char] = count2.get(char, 0) + 1
        
        if count1 == count2:
            return True
        for i in range(n1, n2):
            new_char = s2[i]
            count2[new_char] = count2.get(new_char, 0) + 1
            
            left = s2[i - len(s1)]
            count2[left] -= 1
            if count2[left] == 0:
                del count2[left]
            if count1 == count2:
                return True
        return False
        