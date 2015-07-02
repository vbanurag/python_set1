

#part 1
#return a list of elements which are common between two list no duplicates are allowed

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


new_list=[]
for x in b:
    if x in a:
        new_list.append(x)

print "\nPart 1 : ",new_list, "\n"

#part 2
import random

a1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

b1=[]
for x in range(0,15):
    b1.append(random.randint(1,10))

print "random list :",a1,"\n second random list : ",b1

new_list_ran=[]
for x in a1:
    if x in b1:
        new_list_ran.append(x)

print "\nPart 2: ",new_list_ran,"\n"

################################################

#part 3
#write one line

print "\nOne Line code\n", [x for x in b if x in a]



