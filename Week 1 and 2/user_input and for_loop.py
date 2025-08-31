

age= int(input("Kindly input your age: "))
if age >= 18:
    print("Congratulations, you are allowed to vote")
else:
    print("Sorry, you have to wait until you are older")


alien_colors = ["yellow", "red", "green"]
for alien_color in alien_colors:
    if alien_color == "green":
        print("Congartulations, you have won 50 points")
    elif alien_color=="yellow":
        print("Congratulations, you just earned 10 points")
    else:
        print("You shot the wrong alien")

age = int(input("Enter your age: "))

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " +requested_topping)
print("\nYour pizza has been completed")

user_names = []

for user_name in user_names:
    if user_name == "Admin":
        print("Hello admin, would you like to see a status report\n")
    elif user_name== []:
        print("We need to find new users")
    else:
        print("Hello " + user_name + ", thank you for logging in again\n")

print("Have a nice day\n")