"""Solution By Guruprasada for Problem 1 [ Coding Round ]"""
def target_two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i

    return []


nums1 = [2, 7, 11, 15]
target1 = 9
result1 = target_two_sum(nums1, target1)
print(result1) 


nums2 = [3, 3]
target2 = 6
result2 = target_two_sum(nums2, target2)
print(result2)

#>>>>>>>>---->>>>>>>>>>>>------------>>>>>>>>>>>>>------------->>>>>>>>>>>>>>>------------>>>>>>>>>>>>>.
"""My second type of approach which takes the values from the user instead of mentioning in COde level 
(Please comment the above and uncomment the below to see second approach program)"""
"""
def target_two_sum(nums, target):
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i
    
    return []

nums_input = input("Enter the array of integers (comma-separated): ")
nums = [int(num) for num in nums_input.split(",")]

target = int(input("Enter the target integer: "))

result = target_two_sum(nums, target)
print("Output:", result)

"""

