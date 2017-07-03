import math
import numbers
import decimal
def get_prime_numbers(n):
    if isinstance(n,numbers.Number):
        if n>0:
            if isinstance(n, decimal.Decimal):
                return 'Undefined'                
            else:
                if n==0 or n==1: 
                    return 'Undefined'
                else:
                    prime_numbers=[2]
                    if(n>=2):
                        for num in range(3,n+1,2):
                            num_is_prime=True
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
            
               