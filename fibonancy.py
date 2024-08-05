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

def test_shift_property_mutant1():
    fib_10 = fibonacci(10)
    fib_11 = fibonacci(11)
    if fib_11 == [fib_10[0], fib_10[1], fib_10[2], fib_10[3], fib_10[4], fib_10[5], fib_10[6], fib_10[7], fib_10[8], fib_10[9]]:
        return True
    else:
        return False

def test_shift_property_mutant2():
    fib_10 = fibonacci(10)
    fib_11 = fibonacci(11)
    if fib_11 == [fib_10[0], fib_10[1], fib_10[2], fib_10[3], fib_10[4], fib_10[5], fib_10[6], fib_10[7], fib_10[8], fib_10[10]]:
        return True
    else:
        return False
    
def test_summation_property_mutant1():
    fib_10 = fibonacci(10)
    fib_sum = sum(fib_10)
    if fib_sum == fibonacci(12)[-1]:
        return True
    else:
        return False

def test_mutation_analysis(analysis_type):
    if analysis_type == 1:
        print("Shift property mutation 1: This mutant removes the last element of the 11-term sequence, which should not pass the test case.")
        print(test_shift_property_mutant1())
    elif analysis_type == 2:
        print("Shift property mutation 2: This mutant removes the last element of the 11-term sequence, which should not pass the test case.")
        print(test_shift_property_mutant2())
    elif analysis_type == 3:
        print("Summation property mutation: This mutant checks if the sum of the first 10 Fibonacci numbers is equal to the 12th Fibonacci number, which should not pass the test case.")
        print(test_summation_property_mutant1())
    else:
        print("???")

shift_test_case(10, 11 )  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print()
sumation_test_case()
print()

