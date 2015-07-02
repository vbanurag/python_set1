#make a function of checking no is prime or not

is_prime=False
def prime(pass_value,is_prime=False):
    
    for i in range(2,pass_value/2):
        if pass_value%i==0:
            is_prime=True;
            break;
        
    if is_prime==False:
        print pass_value, " is prime no"
    else:
        print pass_value, " is not a prime no"
