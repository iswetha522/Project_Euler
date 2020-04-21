# LARGEST PRIME FACTOR
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# PRIME NUMBER: Which is divisible by 1 and itself.
# We have to check in between those numbers to find out whether its prime or not.

# EXAMPLE: Below 20 prime numbers are: 2,3,5,7,11,13,17,19

# ALGORITHM:
# Hi snake,
# remember 10 as max
# remember 0 as index
# if max % index == 0. display its not a prime number. 
# Otherwise display max.


# number = int(input("Enter a number to check whether its a prime or not"))
# index = 2
# isPrime = True
# while(index < number/2):
#     if(number % index == 0):
#         isPrime = False
#         break
#     if(number % index != 0):
#         index += 1
#         continue

# if(isPrime):
#     print("Its a prime")
# else:
#     print("Its not a prime")




# Solution for first part
# number = int(input("Enter a number: "))
# index = 2
# for factor in range(2, number):
#     if number % factor == 0:
#         isPrime = True
#         for index in range(2, factor):
#             if(factor % index == 0):
#                     isPrime = False   
#                     break        
#         if(isPrime):
#             print(f"factors are: {factor}")


# Actual Solution:
number = int(input("Enter a number: "))
index = 2
for factor in range(number//2, 2, -1):
    if number % factor == 0:
        isPrime = True
        for index in range(2, factor//2):
            if factor % index == 0:
                isPrime = False
                break

        if isPrime:
            print(f"Largest factor is: {factor}")
            exit(0)
