#we generate a  random number between 1 to 9
# user guess the number, and to check whether user guess right or wrong
# terminates when user hit exit

import random          #import random class for generating the random no #

print " Interactive game \n"
choice='true'               #intialise counter to 0
counter=0
while(choice!='exit'):       
    counter=counter+1          #increment the counter each and every time when user replayed the game
    ran_no=random.randint(1,9)  # generating a random no
    n=int(raw_input(" \nGuess a number: "))
    if n==ran_no:
        print "\nyour guess is ",n," random no is ",ran_no
        print "**** YOUR GUESS IS RIGHT***\n\n"
    else:
        print "\nYour guess is ",n," random no is ",ran_no
        print "\noops ! wrong guess\n"
    choice=raw_input("\n do you want to continue or Exit\n1.For continue Press <anykey>\n2. For exit <type exit> \n Enter Choice : ")
        
print "\n\n User plays this game ",counter," times"
input("press<ENTER>")
