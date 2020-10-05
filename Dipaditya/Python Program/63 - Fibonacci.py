fibonacci_cache = {}


def fibonacci(N):
    # If Nth fibonacci number is present or not
    if N in fibonacci_cache:
        return fibonacci_cache[N]
    
    # Compute the Nth fibonacci number
    if N == 1:
        value = 0
    elif N == 2:
        value = 1
    elif N > 2:
        value = fibonacci(N - 1) + fibonacci(N - 2)

    # cache the value and return the value
    fibonacci_cache[N] = value
    return value


for N in range(1, 10001):
    fibonacci(N)
    print(N, "\t:\t", str(fibonacci_cache[N]))
