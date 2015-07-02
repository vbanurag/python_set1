#ask a no from user and  make a list of all divisor of given no and print that list
print " finding divisors "

num_=int(raw_input("\nEnter a no : "))
divisor=[]
for i in range(2,num_):
    if num_%i==0:
        divisor.append(i)
        
print "Divisor of ",num_," is ",divisor ,"\n Total divisor of ",num_," is ",len(divisor)
