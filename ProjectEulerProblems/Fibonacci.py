# To print Fibonacci series for the first 10 terms

number1 = 0 
number2 = 1
result = 0
max = 10
index = 0
while(index < max):
    result = number1 + number2
    number1 = number2
    number2 = result
    index += 1
    print(result)