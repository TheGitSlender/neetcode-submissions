class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs_dict = {'+','*','-','/'}
        stack = []
        for element in tokens:
            if element not in signs_dict:
                stack.append(element)
            else:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if element == "+":
                    stack.append(first_num + second_num)
                if element == "-":
                    stack.append(first_num - second_num)
                if element == "*":
                    stack.append(first_num * second_num)
                if element == "/":
                    stack.append(int(first_num / second_num))
        return int(stack[-1])
                
        