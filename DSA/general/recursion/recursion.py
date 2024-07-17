# loop solution for counting down a number
def countdown(n):
    for i in range(n):
        print(n-i)

countdown(10)

# recursive solution for counting down a number
def countdown_r(n):
    # return your first result
    print (n)

    # think about what the next result should look like (recursive case)
    # for a countdown, n should be less than 1 in the next
    # iteration, so you can call the function again with the
    # new value of n 

    # then think of an exit (base case). at what stage should the function stop calling itself?
    # for this scenario, the function should exit when n = 0. 
    # if you don't exit, you'll get an infinite loop that will lead to a recursive error

    if n <= 1:
        return 
    else:
        countdown_r(n-1)



countdown_r(15)



def factorial(n):
  if(n > 1):
    return n * factorial (n-1)
  else:
    return 1

print(factorial(5))


def sum_numbers(arr):
  # using divide and conquer (D&C) method
  # step 1: identify the base case: an empty array. i.e. it will
  # it's easy to know the sum of an empty array (0)
  sum = 0
  if len(arr) == 0:
    return sum

  # step 2: move closer to the base case with every recursive call
  # in this case, reducing the elements in the arr passed until 
  # you reach an empty array
  sum = arr.pop(0) + sum_numbers(arr)
  return sum
 

print(sum_numbers([2, 4, 3, 2, 1, 4]))


def find_largest_recursion(arr, largest=None):

  if largest is None:
    largest = arr[0]
  if len(arr) == 1:
    return largest
  
  if largest < arr[1]:
     largest = arr[1]
  return find_largest_recursion(arr[1:], largest)


def max(list):
 
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  sub_max = max(list[1:])
  return list[0] if list[0] > sub_max else sub_max


# updating to handle edge cases
def max_update(list):

  def helper(list):
    if len(list) == 2:
      return list[0] if list[0] > list[1] else list[1]
    sub_max = helper(list[1:])
    return list[0] if list[0] > sub_max else sub_max
    

  if len(list) == 0:
    return None
  if len(list) == 1:
      return list[0]
  
  return helper(list)

  



print(find_largest_recursion([6, 3,8, 2, 9, 5]))

print(max_update([6, 3,8, 2, 9, 5]))


  

