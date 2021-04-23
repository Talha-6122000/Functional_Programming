# Functional Programming
# A clean Functionis the one that does not affect the outsidde world 
# Let's talk about map function
def multiply_by2(item):
  return item*2

my_list=[1,2,3,4]
print(list(map(multiply_by2,my_list)))
# Now we have filter it filters thing for us
# Let's check if a number is odd or not
# Filter checks and return true or false
def only_odd(item):
  return item % 2!=0
# we will pass the list to this function and it will return us the only odd number let's do it

check_odd=[1,2,3,4,5,6,7,8]
print(list(filter(only_odd,check_odd)))
# Let's talk about zip() it works like a zipper 
# We need two list to zip them togather
zip_list1=[1,2,3,4,5]
zip_list2=[6,7,8,9,10]
print(list(zip(zip_list1,zip_list2)))
# What zip function does is it takes the firts item of the first list and takes the first item of the second list and zip them togather 
