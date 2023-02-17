def greet_user(username):

 """Display a simple greeting."""

 print(f"Hello, {username.title()}!")

 

greet_user('jesse')

#-1. Message: Write a function called display_message() that prints one sentence

#  telling everyone what you are learning about in this chapter. Call the 

# function, and make sure the message displays correctly.

def display_message():

    """displaying what i am learning"""

    print("hello everyone I'm learning function, it parameters and argumwnt")

display_message()

#-2. Favorite Book: Write a function called favorite_book() that accepts one 

#parameter, title. The function should print a message, such as One of my 

#favorite books is Alice in Wonderland. Call the function, making sure to 

#include a book title as an argument in the function call

def favorite_book(title):

    print(f"the favorite books title is:, {title.title()}")

favorite_book(" Alice in Wonderland")

#positional argument example

def describe_pet(animal_type, pet_name):

 """Display information about a pet."""

 print(f"\nI have a {animal_type}.")

 print(f"My {animal_type}'s name is {pet_name.title()}.")

 

describe_pet('hamster', 'harry')

describe_pet('cat','while')

#keyword argument example:

describe_pet(animal_type='hamster', pet_name='harry')

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 

# text of a message that should be printed on the shirt. The function should print 

# a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt. Call the 

# function a second time using keyword arguments.

def make_shirt(size, text_message):

    print(f"the size of the t-shirt is: {size}")

    print(f"this is the text message on the t-shirt: {text_message}")

make_shirt(size='38', text_message='international women day')

make_shirt( text_message='international women day', size='38')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 

# by default with a message that reads I love Python. Make a large shirt and a 

# medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size, text_message):

    print(f"the size of the large shirt is: {size}")

    print(f"this is the text message on the large shirt: {text_message}")

    print(f"the size of the medium shirt is: {size}")

    print(f"this is the text message on the  medium shirt: {text_message}")

    print(f"the size of the any size shirt is: {size}")

    print(f"this is the text message on the large shirt: {text_message}")

make_shirt(size='38',text_message='I love Python')

make_shirt('20','I love Python')

make_shirt('50','I love ArewaDS')

# 8-5. Cities: Write a function called describe_city() that accepts the name of 

# a city and its country. The function should print a simple sentence, such as 

# Reykjavik is in Iceland. Give the parameter for the country a default value. 

# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name_of_city, name_country='Iceland'):

    print(f"{name_of_city} is in {name_country}")

describe_city('Reyjavik', name_country='Iceland')

describe_city('uk')

describe_city('china')

describe_city('Reyjavik', name_country='Nigeria')

#example

"""def get_formatted_name(first_name, last_name):

 Return a full name, neatly formatted.

 full_name = f"{first_name} {last_name}"

 return full_name.title()

# This is an infinite loop!

while True:

      print("\nPlease tell me your name:")

      f_name = input("First name: ")

      l_name = input("Last name: ")

 

      formatted_name = get_formatted_name(f_name, l_name)

      print(f"\nHello, {formatted_name}!")"""

#8-6. City Names: Write a function called city_country() that takes in the name 

# of a city and its country. The function should return a string formatted like this:"Santiago, Chile"

# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):

    """Return a city and country"""

    city_country = f"{city} {country}"

    return city_country.title()

places = city_country('Santiago', 'Chile')

print(places)

places = city_country('agadas', 'Niger')

print(places)

places = city_country('Nigeria', 'Dutse')

print(places)

#8-7. Album: Write a function called make_album() that builds a dictionary 

#describing a music album. The function should take in an artist name and an 

#album title, and it should return a dictionary containing these two pieces of 

#information. Use the function to make three dictionaries representing different 

#albums. Print each return value to show that the dictionaries are storing the 

#album information correctly.

#Use None to add an optional parameter to make_album() that allows you to 

#store the number of songs on an album. If the calling line includes a value for 

#the number of songs, add that value to the album’s dictionary. Make at least 

#one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title , num_songs=None):

    album = {

        'artist': artist_name,

        'title': album_title,

    }

    if num_songs:

        album['num_songs'] = num_songs

    return album

album_one = make_album('fati niger', 'fantimoti')

album_two = make_album('Alan waka', 'bara akufai', num_songs=16)

album_three = make_album('Sarkin Waka', 'labarina', num_songs=12)

print(album_one)

print(album_two)

print(album_three)

# Start with your program from Exercise 8-7. Write a while

#loop that allows users to enter an album’s artist and title. Once you have that 

#information, call make_album() with the user’s input and print the dictionary 

#that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title , num_songs=None):

    album = {

        'artist': artist_name,

        'title': album_title,

    }

    if num_songs:

        album['num_songs'] = num_songs

    return album

while True:

 print("\nPlease enter the name of the artist:")

 print("(enter 'q' at any time to quit)")

 artist_name = input("please aritst name:")

 if artist_name =='q':

    break

 album_title = input("please enter album title:")

 if album_title == 'q':

    break

 

artist_name_album_title = make_album(artist_name, album_title , num_songs=None)

print(f"\n this is the information about the make album, {artist_name_album_title}!")

#8-9. Messages: Make a list containing a series of short text messages. Pass the 

#list to a function called show_messages(), which prints each text message.

def show_messages(messages):

    for x in messages:

        msg = f'this is the message: {messages.title()}'

        print(msg)

messages_set =['hello everyone', 'we have a test today', 'try to do your best in order to pass it']

show_messages(messages_set)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 

#Write a function called send_messages() that prints each text message and 

#moves each message to a new list called sent_messages as it’s printed. After 

#calling the function, print both of your lists to make sure the messages were 

#moved correctly.

def send_messages(messages):

    sent_messages = []

    while messages:

        current_message = messages.pop(0)

        print(current_message)

        sent_messages.append(current_message)

    return sent_messages

messages=['hello everyone', 'we have a test today', 'try to do your best in order to pass it']

sent_messages = send_messages(messages)

# Print both lists to confirm that the messages were moved correctly

print("\nOriginal messages:")

print(messages)

print("\nSent messages:")

print(sent_messages)

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 

#function send_messages() with a copy of the list of messages. After calling the 

#function, print both of your lists to show that the original list has retained its messages

sent_messages(sent_messages[:], messages)

#Passing an Arbitrary Number of Arguments

#8-12. Sandwiches: Write a function that accepts a list of items a person wants 

#on a sandwich. The function should have one parameter that collects as many 

#items as the function call provides, and it should print a summary of the sandwich that’s being ordered.

#  Call the function three times, using a different number of arguments each time.

def sandwich(*topping):

    """ptimt the summary of the sandwich being ordered"""

    print(topping)

sandwich('Cheese')

sandwich('Ham and cheese', 'Ham salad','Sausage')

sandwich('Cheese and onion', 'Egg mayonnaise')

#8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a 

#profile of yourself by calling build_profile(), using your first and last names 

#and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):

    user_info['first_name'] = first

    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Abdulrazak', 'Auwal', sex ='Male',

 address='Zaria',

 field='Computer science')

print(user_profile)

#8-14.  Write a function that stores information about a car in a dictionary. 

# The function should always receive a manufacturer and a model name. 

# It should then accept an arbitrary number of keyword arguments. 

# Call the function with the required information and two other name-value pairs, 

# such as a color or an optional feature. Your function should work for a call like this one

#car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car_dict(manufacture, model_name, **car_info):

    car_info ['manufacture name'] = manufacture

    car_info['model name'] = model_name

    return car_info

car = make_car_dict('subaru', 'outback', color='blue', tow_package=True)

print(car)

#8-15. Printing Models: Put the functions for the example printing_models.py in a 

#separate file called printing_functions.py. Write an import statement at the top 

#of printing_models.py, and modify the file to use the imported functions.

from printing_models import print_models as pm

# Imports: Using a program you wrote that has one function in it, store that 

#function in a separate file. Import the function into your main program file, and 

#call the function using each of these approaches:

import build_profile

from build_profile import build_profile

from build_profile import build_profile as bp

import build_profile as mn

from build_profile import *

#-17. Styling Functions: Choose any three programs you wrote for this chapter, 

# and make sure they follow the styling guidelines described in this section.

def describe_city(

    name_of_city, 

    name_country='Iceland'

    ):

    print(f"{name_of_city} is in {name_country}")

describe_city('Reyjavik', name_country='Iceland')

describe_city('uk')

describe_city('china')

describe_city('Reyjavik', name_country='Nigeria')
