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
  if(n >= 1):
    answer = n * factorial (n-1)
    
    return answer
  else:
    return 1

print(factorial(5))
