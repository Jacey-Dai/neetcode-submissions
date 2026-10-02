class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
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
            old_char = s2[i - n1]
            count2[old_char] -= 1
            if count2[old_char] == 0:
                del count2[old_char]
            if count1 == count2:
                return True
        return False