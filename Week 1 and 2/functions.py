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


def describe_pet(pet_type, animal_name):
    print("I have a pet and it's name is " + animal_name)
    print("The type of animal it is is: " + pet_type)

describe_pet(animal_name= "Annie", pet_type="Dog")