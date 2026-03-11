#Create a list
#Ask user input
#Set conditions
numbers = {}
for i in range(1, 11):
    user_input = int(input("Enter number {}: ".format(i)))
    numbers[user_input] = True
for num in numbers:
    print(num)