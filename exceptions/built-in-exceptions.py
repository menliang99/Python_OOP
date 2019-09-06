#https://docs.python.org/3/library/exceptions.html


#AttributeError
class my_class:
    pass

x = my_class()
print (x.non_exist_properity)

#ImportError

#KeyError

my_dict = {'x' : 5, 'y' : 6}
print my_dict['z']


#RuntimeError


#TypeError
int([])

#ValueError
int("a")

#IOError
open('non_existing_file.txt', 'r')

