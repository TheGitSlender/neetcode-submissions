class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            temp_target = target - numbers[i]
            for j in range(i,len(numbers)):
                if numbers[j] == temp_target:
                    return [i+1,j+1]
            