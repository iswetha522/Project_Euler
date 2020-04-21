# EVEN FIBONACCI NUMBERS

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Algorithm
# Hi snake,
# remember 1 as a
# remember 2 as b
# remember 0 as c
# remember 10 as max
# remember 2 as index



# prev2 = 1
# prev = 2
# current = 0
# max = 10
# index = 2
# while (index < max):
#     current = prev2 + prev
#     prev2 = prev
#     prev =  current     
#     index = index + 1
#     print(current)

# Fibonacci Series:
# first = 0
# second = 0
# index = 0 
# max = 100
# while(index < max]):
#     if(index == 0):
#         print(1)
#         index = index + 1
#         continue
#     if(index == 1):
#         print(2)
#         first = 1
#         second = 2
#         index = index + 1
#         continue
#     current = first + second
#     first = second
#     second = current      
#     print(current)
#     index = index + 1



# Simplest way to write Fibonacci Series
number1 = 1
number2 = 2
result  = 0
max_number = 10
print(number1)
print(number2)
while(result < max_number):
    result = number1 + number2
    number1 = number2
    number2 = result
    print(result)



# a, b, result, c = 1, 2, 2, 0
# max = 4000000
# while(c < max):
#     c = a + b
#     if(c % 2 == 0):
#         result += c
#     a, b = b, c
# print(result)
