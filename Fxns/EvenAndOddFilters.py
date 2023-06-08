#Example of filter(),map() and reduce()

from functools import *

numbers=[1,2,3,4,5,6,7]
even_nums=list(filter(lambda n:n%2==0,numbers))
odd_nums=list(filter(lambda n:n%2!=0,numbers))
print("Even nums are: ",even_nums)
print("Odd nums are: ",odd_nums)

map_doubles=list(map(lambda n:n*2,numbers))
print("Doubles are:",map_doubles)

reduce_sum=reduce(lambda x,y:x+y,numbers)
print("Sum:",reduce_sum)
