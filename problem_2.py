"""Solution By Guruprasada for Problem 2 [ Coding Round ]"""

def is_string_is_valid(s):
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    
    stack = []
    
    for char in s:
        if char in bracket_mapping:
            top_element = stack.pop() if stack else '#'
            
            if bracket_mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


s1 = "()"
print(is_string_is_valid(s1))  


s2 = "(]"
print(is_string_is_valid(s2)) 

#>>>>>>>>---->>>>>>>>>>>>------------>>>>>>>>>>>>>------------->>>>>>>>>>>>>>>------------>>>>>>>>>>>>>.
#----->> Below is my second approach which takes input from the user
"""(Please comment the above and uncomment the below to see second approach program)"""
"""
def is_string_is_valid(s):
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_mapping:
            top_element = stack.pop() if stack else '#'
            if bracket_mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

# Take user input for the string
s = input("Enter the string containing brackets: ")

result = is_string_is_valid(s)
print("Output:", result)

"""

