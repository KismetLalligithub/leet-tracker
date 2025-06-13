def isValid(s): 
    closing_parans = [')', ']', '}']
    dic = {
            '(': ')', 
            '{': '}', 
            '[': ']'
            }

    stack = []

    for char in s: 
        if char in closing_parans: 
            if len(stack) != 0 and dic[stack.pop()] == char:
                continue
            else:
                return False
        return len(stack) == 0

