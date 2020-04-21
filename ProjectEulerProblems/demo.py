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
