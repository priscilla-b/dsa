import random

def quick_sort_1(arr):
    # base case is an empty array or array with one element
    if len(arr) < 2:
        return arr
    
    # picking the first element of the array as the pivot
    pivot = arr[0]
    pivot_arr = [pivot] 
    # keeping pivot in an array so that i can just add up all arrays
    # will also help me add elements that are equal to the pivot in the same array
    # so that repeated elements can still show up in the final sorted array

    # partition the array
    less_arr = []
    greater_arr = []
    
    for elem in arr[1:]:
    # don't include pivot in array being looped through to avoid repeated checking
        if elem < pivot:
            less_arr.append(elem)
        elif elem == pivot:
            pivot_arr.append(elem)
        else:
            greater_arr.append(elem)

    return quick_sort_1(less_arr) + pivot_arr + quick_sort_1(greater_arr)


def quick_sort_2(arr):
    # revised solution

    if len(arr) < 2:
        return arr

    pivot = arr[0]

    # partition the array
    less_arr = [elem for elem in arr[1:] if elem <= pivot]
    greater_arr = [elem for elem in arr[1:] if elem > pivot]
    

    return quick_sort_2(less_arr) + [pivot] + quick_sort_2(greater_arr)



# case 1: empty array
print("case 1:", quick_sort_2([]))

# case 2: array with one element
print("case 2:", quick_sort_2([10]))

# case 3: array with two elements
print("case 3:", quick_sort_2([15, 10]))

# case 4: array with three elements
print("case 4:", quick_sort_2([33, 15, 10]))

# case 5: array with four elements
print("case 5:", quick_sort_2([33, 15, 10, 7]))

# case 6: Array with multiple identical elements
print("case 6:", quick_sort_2([5, 5, 5, 5]))
# Expected output: [5, 5, 5, 5]

# Case 7: Array with elements already sorted in ascending order
print("case 7:", quick_sort_2([1, 2, 3, 4, 5]))
# Expected output: [1, 2, 3, 4, 5]

# Case 8: Array with elements sorted in descending order
print("case 8:", quick_sort_2([5, 4, 3, 2, 1]))
# Expected output: [1, 2, 3, 4, 5]

# Case 9: Array with a mix of positive and negative numbers
print("case 9:", quick_sort_2([3, -1, 4, -2, 5, -3]))
# Expected output: [-3, -2, -1, 3, 4, 5]

# Case 10: Array with large numbers
print("case 10:", quick_sort_2([999999, 1000000, 1, 0, -1, -999999]))
# Expected output: [-999999, -1, 0, 1, 999999, 1000000]

# Case 11: Array with floating-point numbers
print("case 11:", quick_sort_2([1.5, 2.3, -0.7, 3.4, -2.2]))
# Expected output: [-2.2, -0.7, 1.5, 2.3, 3.4]

# Case 12: Array with a mix of integers and floating-point numbers
print("case 12:", quick_sort_2([3, 1.2, 2, 4.5, 0, -1.3]))
# Expected output: [-1.3, 0, 1.2, 2, 3, 4.5]

# Case 13: Array with negative integers
print("case 13:", quick_sort_2([-5, -10, -1, -3, -7]))
# Expected output: [-10, -7, -5, -3, -1]


# Case 14: Array with a single large and small number
print("case 14:", quick_sort_2([1000000, -1000000]))
# Expected output: [-1000000, 1000000]


# Case 15: Array with elements in random order
random_list = random.sample(range(-100, 100), 20)
print("case 15:", quick_sort_2(random_list))
# Expected output: A sorted version of random_list




