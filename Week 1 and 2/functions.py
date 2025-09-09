#When defining a function, use def to tell Python you are defining it, name the funcyion and call it
#You can pass information inside a function

# def display_message(username):
#     #Display a simple greeting
#     print("Hello " + username.title() + "!")
# display_message('maiah')

#Positional arguments
#Arguments are what is inside the function and is a piece of information that is passed from a function call to a function
#THis is based on the positions of the argument
# def describe_animal(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_animal("dog", 'bingo')


#Positional arguments are matched by order (`def greet(name, age): greet("Alice", 30)`), while keyword arguments are matched by name
#(`def greet(name, age): greet(name="Alice", age=30)`).
#It all comes down to the defining of the function at the end


# def describe_pet(pet_type, animal_name):
#     print("I have a pet and it's name is " + animal_name)
#     print("The type of animal it is is: " + pet_type)

# describe_pet(animal_name= "Annie", pet_type="Dog")

# def get_formatted_name(first_name, last_name):
#     #Return a fully formatted name 
#     full_name = first_name + " " + last_name
#     return full_name.title()

# musician_name = (get_formatted_name("Jim", "Hendrix"))
# print(musician_name)

#A function can return any value you want it to ranging from lists to dictionaries
# def build_person(first_name, last_name, age=''):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('abel', 'tesfaye')
# print(musician)

# #Using a function while loop
# def get_formatted_name(first_name, last_name):
#     #Return a fully formatted name 
#     full_name = first_name + " " + last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First Name: ")
#     l_name = input("Last Name: ")

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " is now rolling over.")

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

def describe_pet(pet_name, animal_type='dog'):
    print("I have a " + animal_type + ".")

