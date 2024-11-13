
"""
Python solution of Fibonacci series.
"""

def get_fibonacci(till):
    first = 0
    second = 1

    for i in range(till):
        total = first + second
        first = second
        second = total
        print(total)

get_fibonacci(100)