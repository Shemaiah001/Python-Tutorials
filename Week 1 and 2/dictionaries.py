# Dictionaries

# Dictionaries uses curly brackets, and has a "key" and "value". Each key is connected to a value and is used to access that value
# When starting with an empty dictionary or when adding values to a dictionary, it is important to note to use square brackets []
alien = {}

alien['color'] = 'green'
alien['points'] = 5
alien['type'] = 'Kryptonite'

print("The color of the alien is " + str(alien['color']) + ", it's score point is " + str(alien['points']) + " and it is from " 
+ alien['type'])

favourite_languages = {
    "Maiah" : "Python",
    'Phinigga' : 'C++',
    'Ben': 'Java',
    'Dan': 'R'
}
for name, language in favourite_languages.items():
    print(name.title() + " 's favourite language is " + language.title() + ".")

# .items() helps you loop through the values of a dictionary and use a key and a value
#When calling methods, always remember to put the brackets in front

# The .keys() in front of your dictionary would help in only calling the key values
# THe same thing for printing only values

# for name in favourite_languages.keys() or favourite_languages.values()

#To sort in an alphabetical order, use the sorted() function

major_rivers ={
    'nile' : 'egypt',
    'amazon': 'brazil',
    'chad' : 'niger'
}

for river, country in major_rivers.items():
    print("The " + river.title() + " runs in " + country.title())
for river in major_rivers.keys():
    print(river)
for country in major_rivers.values():
    print(country)

# A list inside a dictionary
pizza={
    'crust' : 'thick',
    'toppings' : ['cheese', 'olives']
}

print("You ordered a " + pizza['crust'] + "-thick pizza" + " with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)

favourite_languages = {
    'maiah' : ['python', 'c++', 'java'],
    'jake' : ['c'],
    'sara' : ['r', 'sql']
}
for name, languages in favourite_languages.items():
    print('\n' + name.title() + "'s favourite languages are: ")

    for language in languages:
        print("\t" + language)

# Dictionary of cities
cities = {
    "lagos": {
        "country": "nigeria",
        "population": "15 million",
        "fact": "Lagos is the largest city in Africa by population."
    },
    "tokyo": {
        "country": "japan",
        "population": "37 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "paris": {
        "country": "france",
        "population": "11 million",
        "fact": "Paris is known as the 'City of Light' and home to the Eiffel Tower."
    }
}

# Print information about each city
for city, info in cities.items():
    print("\nCity: " + city.title())
    print("  Country: " + info['country'].title())
    print("  Population: " + info['population'])
    print("  Fact: " + info['fact'])

countries={
    'Japan' : {
        'capital': 'tokyo',
        'currency': 'yen',
        'population': "100 milion"
    },

    'Nigeria':{
        'capital': 'Lagos',
        'currency': 'naira',
        'population': '220 million'
    },

    'America' : {
        'capital': 'Washington DC',
        'currency': 'dollar',
        'population': '200 million'
    }
}

for country, detail in countries.items():
    print('\nCountry: ' +country.title())
    print(" Capital: " + detail['capital'].title())
    print(" Currency: " + detail['currency'].title())
    print(" Population: " + detail['population'].title())

count = 0              # counter for valid entries
heights = []           # list to store heights