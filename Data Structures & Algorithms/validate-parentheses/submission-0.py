class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]":"[", "}":"{", ")":"("}
        temp_list = []
        for bracket in s:
            if bracket in brackets:
                top = temp_list.pop() if temp_list else "s"
                if brackets[bracket] != top:
                    return False
            else:
                temp_list.append(bracket)
        return not temp_list
            