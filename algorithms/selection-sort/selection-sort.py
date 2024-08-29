def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index
    


def selection_sort(arr, order):
    newArr = []
    if order == "asc":
        for i in range(len(arr)):
            index = find_smallest(arr) 
            newArr.append(arr.pop(index))
   
    else:
        for i in range(len(arr)):
            index = find_largest(arr) 
            newArr.append(arr.pop(index)) 

        
    return newArr
      

print(selection_sort([5, 3, 6, 2, 10], "desc"))
        