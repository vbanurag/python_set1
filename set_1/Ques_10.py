#print a fibonacci series by taking range from the user
print " printing a Fibonacci Series \n"
a=1
b=0
c=0
fib_list=[]
limit_series=int(raw_input("Enter a limit upto you want to print: "))

for i in range(0,limit_series):
    #print c
    fib_list.append(c)
    c=a+b
    a=b
    b=c
print "Fibonacci series upto ",limit_series," is ",fib_list

