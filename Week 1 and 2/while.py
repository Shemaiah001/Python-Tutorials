while True:
    heights = input("Please input your height in cm (or type 'exit' to quit): ")

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


#Start with users that are unverified and need to be verified
# and an empty list to hold confirm users
unconfirmed_users = ["Alice", "Brian", "Charles"]

confirmed_users = []

#Verify each users until there are no more unconfirmed users
#Move each verified user into the confirmed users

while unconfirmed_users: 
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user) 

#Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#remove() is used to remove specific value from a list
while 'cat' in pets:
 pets.remove('cat')
 
print(pets)

responses = {}

#set a flag to indicate that the polling is active
polling_active = True

while polling_active:
    #Prompt for the user name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb today? ")

    #Store the responses in a dictionary
    #The name is the key and the response
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
 
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#Code to push to github
#git add .
# git commit -m "Updated code"
# git push
