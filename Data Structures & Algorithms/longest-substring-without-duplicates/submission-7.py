class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maximum = 0
        left = 0
        validated = set()
        count = 0

        for i in range(n):
            if s[i] not in validated:
                validated.add(s[i])
                count += 1
                if count > maximum:
                    maximum = count
            else:
                for j in range(left,i):
                    if s[j] == s[i]:
                        left = j+1
                        break
                    validated.remove(s[j])
                count = i-left + 1
        
        return maximum