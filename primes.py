"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes:int):
    list = [] 
    a = 2 
    while len(list) != number_of_primes:   
        for b in range(2, a):   
          if a % b == 0:      
           break       
        else:       
            a+=1    
    return list    
