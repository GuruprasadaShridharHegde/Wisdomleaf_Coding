"""Solution By Guruprasada for Problem 3 [ Coding Round ]"""
def frequent_element(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child][0] > arr[child + 1][0]:
            child += 1
        if arr[root][0] > arr[child][0]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        frequent_element(arr, i, n - 1)

def k_most_frequent(nums, k):
    freq_count = {}
    for num in nums:
        freq_count[num] = freq_count.get(num, 0) + 1
    
    min_heap = list(freq_count.items())
    build_heap(min_heap)

    for i in range(k, len(min_heap)):
        if min_heap[i][0] > min_heap[0][0]:
            min_heap[0] = min_heap[i]
            frequent_element(min_heap, 0, k - 1)

    return [num for _, num in min_heap[:k]]


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(sorted(k_most_frequent(nums1, k1)))  


nums2 = [1]
k2 = 1
print(sorted(k_most_frequent(nums2, k2)))  



#>>>>>>>>---->>>>>>>>>>>>------------>>>>>>>>>>>>>------------->>>>>>>>>>>>>>>------------>>>>>>>>>>>>>.
#----->> Below is my second approach which takes input from the user
"""(Please comment the above and uncomment the below to see second approach program)"""
"""
def frequent_element(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child][0] > arr[child + 1][0]:
            child += 1
        if arr[root][0] > arr[child][0]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        frequent_element(arr, i, n - 1)

def k_most_frequent(nums, k):
    freq_count = {}
    for num in nums:
        freq_count[num] = freq_count.get(num, 0) + 1
    
    min_heap = list(freq_count.items())
    build_heap(min_heap)

    for i in range(k, len(min_heap)):
        if min_heap[i][0] > min_heap[0][0]:
            min_heap[0] = min_heap[i]
            frequent_element(min_heap, 0, k - 1)

    return [num for _, num in min_heap[:k]]

# Take user input for the array of integers (comma-separated)
nums_input = input("Enter the array of integers (comma-separated): ")
nums = [int(num) for num in nums_input.split(",")]


k = int(input("Enter the value of k: "))

# Get the k most frequent elements and sort the result
result = sorted(k_most_frequent(nums, k))

# Print the result
print("Output:", result)

"""