#make a list using range value which is given by user
def alist(range_value,alist=[],newlist=[]):
    for i in range(0,range_value):
        n=int(raw_input("enter a no : "))
        alist.append(n)
	
	newlist[=alist[:range_value:range_value-1] #print onlt first and last element of 'alist'

    
    print "\nOrginal list : ",alist 
    print "\n New List : ", newlist
    input("press<ENTER>")
