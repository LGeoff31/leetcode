class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation =="C":
                stack.pop()
            elif operation == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(operation))
        return sum(stack)

        