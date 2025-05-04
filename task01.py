def generate_fibonacci(n): #function is defined here.
    fib_series = [] #list is given 
    a, b = 0,  #variables.
    for _ in range(n): #loop 
        fib_series.append(a) #object identified.
        a, b = b, a + b
    return fib_series

n_terms = 10
print("Fibonacci Series:", generate_fibonacci(n_terms)) #printing in the last.
 #now let's see the results.
