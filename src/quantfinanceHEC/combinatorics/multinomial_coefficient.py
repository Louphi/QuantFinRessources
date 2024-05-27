import math
import numpy as np

def f_multinomial_coefficient(n, k_list):
    
    sum_k_list = sum(k_list)
    
    if sum_k_list != n:
        print("Invalid input: sum(k_i) = n")
        return
    
    factorial_product = np.prod(math.factorial(k) for k in k_list)

    return math.factorial(n) / factorial_product


    

