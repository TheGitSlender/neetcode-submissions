class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = dict()
        for letter in s1:
            if letter in dict_s1: 
                dict_s1[letter] += 1 
            else:
                dict_s1[letter] = 1
        temp_dict = dict_s1.copy()

        left = 0
        n = len(s1)

        for i in range(len(s2)):
            if i-left+1 > n:
                if s2[left] in temp_dict:
                    temp_dict[s2[left]] += 1
                left += 1
            if s2[i] in temp_dict:
                temp_dict[s2[i]] -= 1
            if all(x == 0 for x in temp_dict.values()):
                return True

        return False
