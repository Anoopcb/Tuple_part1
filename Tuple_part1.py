## This is all about Tuples

## tuple are also data structures like list
### tupe can store any data type
####most important tup;es are immutable
#means once tuple is created you can't update or amend data
## data inside tuple

example = ('one', 'two', 'Three')

# no append(), no insert(), no pop() and no remove()
 ## we use around brackets for tuple
 ### tuples are faster than lists

 ######### methods in tuples

 ## count(), index(),
 ### len function can be used

 ### slicing can be done

print(example[:2])
print(len(example))

mixed = (1, 2, 3, 4, 5.0)
 # loop in tuple

for i in mixed:

     print(i)
#tuple with on element

num = (1,)# must put comma after value otherwise it will be
#consider int, float, or string

## tuple without parenthesis

guitars = "yamaha", "baton rouge", "taylor"

## tuple unpacking

guitarists = ("Maneli Jamal", "Eddie Van de Meer", "Andrew Fory")
guitarist1, guitarist2, guitarist3 = (guitarists)

print(guitarist1)

## list inside tuple
favorites = ("Southern Magnolia", ["Tokyo1", "langscaple"] )

favorites[1].pop()

print(favorites)
favorites[1].append("we made it")
print(favorites)

## functions in tuple

# min, max, sum

print(min(mixed))
print(max(mixed))


## function returning two values

def func(int1, int2):

    add = int1 + int2

    multiply = int1*int2
    return add, multiply

print(func(2, 7))## this will return tuple


# this below will solve this problem

add, multily = func(2, 7)
print(add)
print(multily)


nums = tuple(range(2, 21, 2))
print(nums)
print(type(nums))

num = list((2, 4, 6, 8, 10, 12, 14, 16, 18, 20))
print(type(num))
type(num)

num1 = str((2, 4, 6, 8, 10, 12, 14, 16, 18, 20))
print(type(num1))
print(type(num1))















