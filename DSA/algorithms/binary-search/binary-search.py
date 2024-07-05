def binary_search(list, item):
    # binary search assumes list is sorted so lowest value of list will be the first element
    # with the last element as the highest value

    low = 0   # position of first element
    high = len(list) - 1  # position of last element

    while low <= high:
        # as long as there's a range between our low and high point,
        # item has still not been located, so we need to keep guess

        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            # guess is higher than item we're looking for, so make sure that
            # high point is lower than the position used to guess (mid)
            high = mid - 1
        else:
            # guess is lower than item we're looking for, so make sure that
            # low point is higher than the position used to guess (mid)
            low = mid + 1

    return None  # item doesn't exist

my_list = []
result = binary_search(my_list, 3)
print(result)   

