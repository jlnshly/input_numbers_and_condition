#Set a list
#Set a loop
#Finalize conditions
number_list = []
for i in range(1, 11):
    user_input = float(input("Enter a number: "))
    if user_input in number_list:
        print("Duplicate")
    else:
        print("Unique")
    number_list.append(user_input)
