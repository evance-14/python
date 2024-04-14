#Createafunction calcaverage that calaculates the average of two numbers.
#def calcaverage(x,y):
    #return (x + y )/2
#x = 4
#y = 8
#z = (x +y)/2
#print(z)

# write a python function that generates the first 10 fibonacci numbers

def generate_fibonacci(N):
    fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    
    # Generate the next Fibonacci numbers
    for i in range(2, N):
        next_fib = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
        fibonacci_numbers.append(next_fib)
    
    return fibonacci_numbers

# Test the function with N = 10
N = 10
print(f"The first {N} Fibonacci numbers:")
print(generate_fibonacci(N))
