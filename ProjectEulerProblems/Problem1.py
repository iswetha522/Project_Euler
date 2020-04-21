# MULTIPLES OF 3 AND 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

# Algorithm
# Hi snake,
# remember 10 as max number
# remember 3 as num1 and remember 5 as number
# remember 0 as result


max = int(input("Enter maximum number"))
num1 = 3
num2 = 5
result = 0
index = 1
while(index < max):
    if (index % num1 == 0 or index % num2 == 0):
        result = result + index
    index = index + 1
print(result)
