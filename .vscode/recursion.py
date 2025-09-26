##  Assignment ##

##Print first n natural numbers using recursion.##
def natural_num(n):
    if n == 0:
        return
    print(n)
    natural_num(n-1)
natural_num(10)
    
##N natural numbers using recursion in reverse order##
def natural_num_rev(n):
    if n == 0:
        return
    natural_num(n-1)
    print(n)
natural_num_rev(10)

##First n even numbers using recursion##
def even_num(n):
    if n == 0:
        return
    # if n % 2 == 0:
    #    print(n)
    even_num(n-1)
    if n % 2 == 0:
       print(n)
print(even_num(10))

