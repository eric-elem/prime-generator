import math
import numbers
import decimal
def get_prime_numbers(n):
    # check if input is a number
    if isinstance(n,numbers.Number):
        # check if input is positive
        if n>0:
            # check if input is decimal
            if isinstance(n, decimal.Decimal):
                return 'Undefined'                
            else:
                # check if n is 0 or 1 as prime numbers start from 2
                if n==0 or n==1: 
                    return 'Undefined'
                else:
                    prime_numbers=[2]
                    if(n>=2):
                        """ loop through odd numbers from 3 to n as 
                            even numbers aren't prime except 2
                        """
                        for num in range(3,n+1,2):
                            num_is_prime=True
                            # selecting denominator between 2 and sqrt(num)
                            for denom in range(2,int(math.sqrt(num))+1):
                                if(num%denom==0):
                                    num_is_prime=False
                                    break
                            if(num_is_prime):    
                                prime_numbers.append(num)
                    return prime_numbers                 
        else:
            return 'Undefined'
    else:
        return 'Undefined'   
            
               