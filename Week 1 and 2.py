# # # message= "Hello Eric"

# # # greeting= "Welcome to the world of Python"

# # # full_greeting= message + "\n" + greeting

# # # print(full_greeting)

# # favourite_number= 13

# # new_message= f"My favourite number is {favourite_number}"

# # #This is a f-string. It is a string that contains a variable. And it is used to insert the variable into the string.
# # print(new_message)


# # import this #This is a module that contains the Zen of Python. It is a collection of quotes about the philosophy of Python.

# friends= ["Eric", "John", "Michael", "Terry", "Graham"]
# # Square brackets are used to access elements of a list.
# # The first element of a list is at index 0.
# # The last element of a list is at index -1.
# # The second last element of a list is at index -2.
# # The third last element of a list is at index -3.
# # And so on.

# # friends.append("Maiah")
# # # The append method adds an element to the end of the list.

# friends.insert(3, "Maiah")
# #The insert method adds an element to the list in a specific position

# friends.remove("Eric")
# #The remove method removes an element from the list

# friends.pop()
# #The pop method removes the last element from the list

# friends.sort()
# #The sort method sorts the list in ascending order

# This program creates a list of friends and then sends a personalized
# invitation message to each one by looping through the list.
# invited_friends=["Maiah", "Ruth", "Him"]

# for name in invited_friends:
#     message= f"Hi {name}, you are invited to a party"
#     print(message)



# favourite_pizzas = ["Pepperoni", "Sausage and Cheese", "Meat Lovers"]

# for favourite_pizza in favourite_pizzas:
#     message = f"My favourite pizza is {favourite_pizza}"
#     print(message + "\n")
# print("You can say I really love pizza")


for value in range(0,100):
    print("The number is " + str(value))

