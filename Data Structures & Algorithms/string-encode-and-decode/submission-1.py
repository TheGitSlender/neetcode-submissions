class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string + "£"
        result.strip("£")

        return result


    def decode(self, s: str) -> List[str]:
        result_list = s.split("£")
        return result_list[:-1]
