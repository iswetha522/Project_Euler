# Program 1

number1 = int(input("Enter starting number "))
number2 = int(input("Enter ending number "))

for number in range(number1, number2 + 1):
    isPrime = True
    for index in range(2, number//2+1):
        if(number % index == 0):
            isPrime = False  
            break 
    
    if(isPrime):
        print(f"{number}")
    

# Program 2

invested_amount = int(input("Enter your invested amount "))
return_amount = int(input("Enter the amount returned from investment "))
months_count = int(input("Enter number of months it took for return "))
profit = return_amount - invested_amount
print(f"Profit or Loss is {profit}")
net_profit_per_month = profit/months_count
yearly_profit = net_profit_per_month * 12
print(f"Return % per year is {yearly_profit}")


