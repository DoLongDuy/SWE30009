from fibonancy import fibonacci
from unittest import TestCase 

# for some reason, mutpy keep having error that Stack Overflow dont know, so I just give up on showing the test case
class FibonacciTest(TestCase): 
      
    # test case for checking same sequence
    def test_shift(self): 
        self.assertEqual(fibonacci(11), fibonacci(12)[:-1]) 
      
    # test case to check if the sum of the final 2 number of sequence n is equal to 
    def test_sum(self): 
        self.assertEqual(fibonacci(19)[-1], fibonacci(18)[-1]+fibonacci(18)[-2]) 
  
    # test case to check invalid input 
    def test_invalid(self): 
        self.assertEqual(fibonacci(-1), [])


test = FibonacciTest()
