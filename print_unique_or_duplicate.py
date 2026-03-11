#Set a list
#Set a loop
#Finalize conditions
number_list = []
while True:
    try:
        user_input = float(input("Enter a number: "))
        if user_input in number_list:
            print("Duplicate")
        else:
            print("Unique")
        number_list.append(user_input)
    except ValueError:
        break
