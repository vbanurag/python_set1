#checking the no is even or not
#if no is even and also multiple of 4 print different message

user_num=int(raw_input("\n Enter a number : "))

if user_num%2==0:
    print user_num," is even no. \n"
    if user_num%4==0:
        print user_num," is also multiple of 4 \n"
else:
    print user_num," is odd no \n"
    
#part 2
# take two number from user and check the first no is divide by another no or not

first_num=int(raw_input("\n Enter two number : "))

sec_num=int(raw_input("\n Enter two number : "))

if first_num%sec_num==0 or sec_num%first_num==0:
    if first_num>sec_num:
        print first_num," is multiple of ",sec_num
    else:
        print sec_num, "is a multiple of ",first_num
else:
    print first_num," is not multiple of ",sec_num
    
