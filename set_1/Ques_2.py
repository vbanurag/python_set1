a=[1,1,2,3,5,8,13,21,34,55,98]

#part 1

#prints all elements of the list which are less than 5

print "\nThe no. are less than 5 is : ",[x for x in a if x<5]

#part 2
#print a seperate list and stored a no which is less than 5

new_a=[]

for x in a:
    if x<5:
        new_a.append(x)

print "\n New list is ",new_a

#part 3
#part 2 convert in one line code
new_single_line=[]


[new_single_line.append(x) for x in a if x<5]
print "\n New list using list comprehension is ",new_single_line

#part 4
#user input of number x and prints all elements which are less than that the orignal list

user_num=int(raw_input("\nEnter a number : "))

for x in a:
    if user_num>x:
        print x
