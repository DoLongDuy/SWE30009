def fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth term.
    
    Args:
        n (int): The number of Fibonacci terms to generate.
    
    Returns:
        list: The Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

# Example usage
def shift_test_case(n_orginal, n_transformed):
    print("Shifted test case")
    print("Original test case")
    print(fibonacci(n_orginal))
    print("Transformed test case")
    print(fibonacci(n_transformed))

def test_summation_property():
    fib_10 = fibonacci(10)
    fib_sum = sum(fib_10)
    if fib_sum == fibonacci(12)[-1] - 1:
        return True
    else:
        return False
    

def sumation_test_case():
    print("Sumation test case")
    print(test_summation_property())


shift_test_case(10, 11 )  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print()
sumation_test_case()
