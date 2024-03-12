# Given n pairs of parentheses, write a function to generate all combinations
#  of well-formed parentheses.
# write code

def generateParentheses(n: int) -> str:
    result = []

    def backtrack(s, openingN, closingN):
        if len(s) == 2 * n:
            result.append(s)
            return
        if openingN < n:
            backtrack(s + '(', openingN + 1, closingN)
        if closingN < openingN:
            backtrack(s + ')', openingN, closingN + 1)

    backtrack('', 0, 0)
    return result

print(generateParentheses(3))
