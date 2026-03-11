#Create a list
#Ask user input
#Set conditions
numbers = []
for i in range(1, 11):
    user_input = float(input("Enter number {}: ".format(i)))
    numbers.append(user_input)
number_list = []
for user_input in numbers:
    if numbers.count(user_input) == 1:
    number_list.append(user_input)
print(number_list)