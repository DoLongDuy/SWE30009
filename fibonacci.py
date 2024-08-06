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
    print("Metamorphic Relation: Shifted Property")
    print(f"Original test case: Sequence of n = {n_orginal}")
    print(fibonacci(n_orginal))
    print(f"Transformed test case: Sequence of n = {n_transformed}")
    print(fibonacci(n_transformed))

def sum_test_case(n_orginal, n_transformed):
    print("Metamorphic Relation: Sum Property")
    print(f"Original test case: Final 2 number of n = {n_orginal}")
    ori_fib = fibonacci(n_orginal)
    print(f"Original sequence's number at position {ori_fib.index(ori_fib[-2]) + 1}: {ori_fib[-2]}, number at position {ori_fib.index(ori_fib[-1]) + 1}: {ori_fib[-1]}")
    print(f"Transformed test case: n = {n_transformed}")
    print(f"Transformed sequence's number at position {fibonacci(n_transformed).index(ori_fib[-1]) + 1}: {fibonacci(n_transformed)[-1]}")
    


