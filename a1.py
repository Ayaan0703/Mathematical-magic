number = int(input("Enter your number:"))

digits = len(str(number))

resultN176umber = 0

temp = number

while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number,"is an armstrong number")
else:
    print(number,"isn't an armstrong number")