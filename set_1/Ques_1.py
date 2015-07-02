#asks user age and name and print that year in which user turns 100 yr
print " Calculating the year"

name=raw_input("\nEnter your name : ")
age = int(raw_input("\nEnter your age : "))

rest_age = int(100)-age
year_ = 2015+rest_age

print name, " will turn 100 year old in ", year_,"\n\n"
