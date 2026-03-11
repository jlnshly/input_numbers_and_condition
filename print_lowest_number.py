#Ask user input
#Set a loop
#Set the conditions to find lowest number
number_list = []
while True:
    try:
        user_input = float(input("Enter a number: "))
        number_list.append(user_input)
    except ValueError:
        break
if number_list:
    lowest_number = min(number_list)
print(lowest_number)

