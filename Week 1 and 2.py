# # # # message= "Hello Eric"

# # # # greeting= "Welcome to the world of Python"

# # # # full_greeting= message + "\n" + greeting

# # # # print(full_greeting)

# # # favourite_number= 13

# # # new_message= f"My favourite number is {favourite_number}"

# # # #This is a f-string. It is a string that contains a variable. And it is used to insert the variable into the string.
# # # print(new_message)

# #

# # # import this #This is a module that contains the Zen of Python. It is a collection of quotes about the philosophy of Python.

# # friends= ["Eric", "John", "Michael", "Terry", "Graham"]
# # # Square brackets are used to access elements of a list.
# # # The first element of a list is at index 0.
# # # The last element of a list is at index -1.
# # # The second last element of a list is at index -2.
# # # The third last element of a list is at index -3.
# # # And so on.

# # # friends.append("Maiah")
# # # # The append method adds an element to the end of the list.

# # friends.insert(3, "Maiah")
# # #The insert method adds an element to the list in a specific position

# # friends.remove("Eric")
# # #The remove method removes an element from the list

# # friends.pop()
# # #The pop method removes the last element from the list

# # friends.sort()
# # #The sort method sorts the list in ascending order

# # # This program creates a list of friends and then sends a personalized
# # # invitation message to each one by looping through the list.
# # invited_friends=["Maiah", "Ruth", "Him"]

# # for name in invited_friends:
# #     message= f"Hi {name}, you are invited to a party"
# #     print(message)



# # favourite_pizzas = ["Pepperoni", "Sausage and Cheese", "Meat Lovers"]

# # for favourite_pizza in favourite_pizzas:
# #     message = f"My favourite pizza is {favourite_pizza}"
# #     print(message + "\n")
# # print("You can say I really love pizza")

# # # Adding the list function would change the range to a list
# # squares = []

# # for value in range(0,10):
# #     square = value**2
# #     squares.append(square)

# # print(squares)

# # odd_numbers = []
# # for value in range(1,100,2):
# #     odd_numbers.append(value)
# # print(odd_numbers)

# # #Difference between a list[] and a tuple() is that tuples cannot be edited

# # # Define the buffet menu as a tuple
# # buffet_menu = ("Rice", "Beans", "Salad", "Chicken", "Fish")

# # print("Original Buffet Menu:")
# # for food in buffet_menu:
# #     print(food)

# # # Try to modify one of the items (this will raise an error)
# # # buffet_menu[0] = "Pizza"   # Uncomment to see the error (TypeError)

# # # Rewrite the tuple with new items
# # buffet_menu = ("Pizza", "Pasta", "Salad", "Chicken", "Beef")

# # print("\nRevised Buffet Menu:")
# # for food in buffet_menu:
# #     print(food)

# # cars= ["audi", "toyota", "benz", "honda"]
# # for car in cars:
# #     if car == "audi":
# #         print(car.upper())
# #     else:
# #         print(car.title())

# # age= int(input("Kindly input your age: "))
# # if age >= 18:
# #     print("Congratulations, you are allowed to vote")
# # else:
# #     print("Sorry, you have to wait until you are older")


# # alien_colors = ["yellow", "red", "green"]
# # for alien_color in alien_colors:
# #     if alien_color == "green":
# #         print("Congartulations, you have won 50 points")
# #     elif alien_color=="yellow":
# #         print("Congratulations, you just earned 10 points")
# #     else:
# #         print("You shot the wrong alien")

# # age = int(input("Enter your age: "))

# # if age < 2:
# #     print("The person is a baby.")
# # elif age < 4:
# #     print("The person is a toddler.")
# # elif age < 13:
# #     print("The person is a kid.")
# # elif age < 20:
# #     print("The person is a teenager.")
# # elif age < 65:
# #     print("The person is an adult.")
# # else:
# #     print("The person is an elder.")

# # available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# # requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# # for requested_topping in requested_toppings:
# #     if requested_topping in available_toppings:
# #         print("Adding " + requested_topping + ".")
# #     else:
# #         print("Sorry, we don't have " +requested_topping)
# # print("\nYour pizza has been completed")

# # user_names = []

# # for user_name in user_names:
# #     if user_name == "Admin":
# #         print("Hello admin, would you like to see a status report\n")
# #     elif user_name== []:
# #         print("We need to find new users")
# #     else:
# #         print("Hello " + user_name + ", thank you for logging in again\n")

# # print("Have a nice day\n")


# #Dictionaries

# #Dictionaries uses curly brackets, and has a "key" and "value". Each key is connected to a value and is used to access that value
# #When starting with an empty dictionary or when adding values to a dictionary, it is important to note to use square brackets []
# # alien = {}

# # alien['color'] = 'green'
# # alien['points'] = 5
# # alien['type'] = 'Kryptonite'

# # print("The color of the alien is " + str(alien['color']) + ", it's score point is " + str(alien['points']) + " and it is from " 
# # + alien['type'])

# favourite_languages = {
#     "Maiah" : "Python",
#     'Phinigga' : 'C++',
#     'Ben': 'Java',
#     'Dan': 'R'
# }
# for name, language in favourite_languages.items():
#     print(name.title() + " 's favourite language is " + language.title() + ".")

# # .items() helps you loop through the values of a dictionary and use a key and a value
# #When calling methods, always remember to put the brackets in front

# # The .keys() in front of your dictionary would help in only calling the key values
# # THe same thing for printing only values

# # for name in favourite_languages.keys() or favourite_languages.values()

# #To sort in an alphabetical order, use the sorted() function

# major_rivers ={
#     'nile' : 'egypt',
#     'amazon': 'brazil',
#     'chad' : 'niger'
# }

# for river, country in major_rivers.items():
#     print("The " + river.title() + " runs in " + country.title())
# for river in major_rivers.keys():
#     print(river)
# for country in major_rivers.values():
#     print(country)

#A list inside a dictionary
# pizza={
#     'crust' : 'thick',
#     'toppings' : ['cheese', 'olives']
# }

# print("You ordered a " + pizza['crust'] + "-thick pizza" + " with the following toppings: ")

# for topping in pizza['toppings']:
#     print("\t" + topping)

# favourite_languages = {
#     'maiah' : ['python', 'c++', 'java'],
#     'jake' : ['c'],
#     'sara' : ['r', 'sql']
# }
# for name, languages in favourite_languages.items():
#     print('\n' + name.title() + "'s favourite languages are: ")

#     for language in languages:
#         print("\t" + language)

# Dictionary of cities
# cities = {
#     "lagos": {
#         "country": "nigeria",
#         "population": "15 million",
#         "fact": "Lagos is the largest city in Africa by population."
#     },
#     "tokyo": {
#         "country": "japan",
#         "population": "37 million",
#         "fact": "Tokyo is the most populous metropolitan area in the world."
#     },
#     "paris": {
#         "country": "france",
#         "population": "11 million",
#         "fact": "Paris is known as the 'City of Light' and home to the Eiffel Tower."
#     }
# }

# # Print information about each city
# for city, info in cities.items():
#     print("\nCity: " + city.title())
#     print("  Country: " + info['country'].title())
#     print("  Population: " + info['population'])
#     print("  Fact: " + info['fact'])

# countries={
#     'Japan' : {
#         'capital': 'tokyo',
#         'currency': 'yen',
#         'population': "100 milion"
#     },

#     'Nigeria':{
#         'capital': 'Lagos',
#         'currency': 'naira',
#         'population': '220 million'
#     },

#     'America' : {
#         'capital': 'Washington DC',
#         'currency': 'dollar',
#         'population': '200 million'
#     }
# }

# for country, detail in countries.items():
#     print('\nCountry: ' +country.title())
#     print(" Capital: " + detail['capital'].title())
#     print(" Currency: " + detail['currency'].title())
#     print(" Population: " + detail['population'].title())

count = 0              # counter for valid entries
heights = []           # list to store heights

while True:
    height = input("Please input your height in cm (or type 'exit' to quit): ")

    # Allow user to quit
    if height.lower() == "exit":
        print("\nYou entered your height", count, "times.")
        if count > 0:
            print("The heights you entered are:", heights)
        else:
            print("You did not enter any valid height.")
        print("Goodbye 👋")
        break

    # Handle invalid input
    if not height.isdigit():
        print("⚠️ Please enter a valid number.\n")
        continue

    # Convert to integer
    height = int(height)
    count += 1          # increase counter for valid entry
    heights.append(height)  # store the height

    # Check height
    if height < 180:
        print("You are not tall enough.\n")
    else:
        print("You are tall enough!\n")
