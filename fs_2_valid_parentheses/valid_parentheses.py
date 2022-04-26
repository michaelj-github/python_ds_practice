def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    thecount = 0
    for p in list(parens):
        if p == '(':
            thecount += 1
        if p == ')':
            thecount -= 1
        if thecount < 0:
            # print(False)
            return False
    if thecount != 0:
        # print(False)
        return False
    # print(True)
    return True

# valid_parentheses("()")
# valid_parentheses("()()")
# valid_parentheses("(()())")
# valid_parentheses(")()")
# valid_parentheses("())")
# valid_parentheses("((())")
# valid_parentheses(")()(")
# valid_parentheses("(((((()()())(((())()()())))()())()))")
# valid_parentheses("(((((()()())(((())()()())))()())())))")
