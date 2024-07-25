# https://leetcode.com/problems/valid-parentheses/
def valid(s):
        stack = []
        pairs = {
            '(':')',
            '{':'}',
            '[':']',
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            # elif bracket!=pairs[stack.pop()] or len(stack) == 0:
            # interchanging the above two lines will give wrong answer as we need to check the length of stack first and then pop

                   return False
        return len(stack) == 0
                
s = "({[]})"
print(valid(s)) # True
