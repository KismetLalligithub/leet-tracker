def isPalindrome(s): 
    new_s = ""
    letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for char in c: 
        lowered_char = char.lower()
        if lowered_char in letters or lowered_char in numbers: 
            new_s += lowered_char
        
    return new_s[::-1] == new_s

