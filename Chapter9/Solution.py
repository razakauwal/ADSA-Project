
#9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
#estaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Nanah Maggs", "Nigerian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
 #9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each instance.
# Create three different instances of the Restaurant class
restaurant1 = Restaurant("MrBiggs", "Zaria")
restaurant2 = Restaurant("Bigchop", "Kano")
restaurant3 = Restaurant("EatWell", "Sokoto")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9-3. Users: Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored 
#in a user profile. Make a method called describe_user() that prints a summary 
#of the user’s information. Make another method called greet_user() that prints 
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, age, location, school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.school = school
    
    def describe_user(self):
        print(f"User profile: {self.first_name} {self.last_name} is {self.age} years old, located in {self.location}, and studing in {self.school}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


# Create several instances representing different users
user1 = User("sani", "abdullahi", 35, "KANO", "ABU")
user2 = User("Falmata", "Iro", 20, "KANO", "ABU")
user3 = User("FATIMA", "sunusi", 25, "YOBE", "BUK")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
#9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
#Add an attribute called number_served with a default value of 0. Create an 
#instance called restaurant from this class. Print the number of customers the 
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number 
#of customers that have been served. Call this method with a new number and 
#print the value again.
#Add a method called increment_number_served() that lets you increment 
#the number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self. number_served =0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, number):
        self.number_served +=  number


restaurant = Restaurant("Hasina Cetaring", "Nigerian")
print(f'the resturant has served {restaurant.number_served} customers')
restaurant.number_served = 12
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 16
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 20
print(f"The restaurant has served {restaurant.number_served} customers.")

#9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
#  that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts
#to 0.Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented 
#properly, and then call reset_login_attempts(). Print login_attempts again to 
#make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name, age, location, school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.school = school
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"school: {self.school}")
        print(f"Location: {self.location}")
        print(f"age: {self.age}")
    
    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
# Creating an instance of the User class
user = User("sani", "abdullahi", 35, "KANO", "ABU")

# Calling the increment_login_attempts() method several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the value of login_attempts to make sure it was incremented properly
print(f"Number of login attempts: {user.login_attempts}")

# Calling the reset_login_attempts() method
user.reset_login_attempts()

# Printing the value of login_attempts to make sure it was reset to 0
print(f"Number of login attempts after reset: {user.login_attempts}")


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
#a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
#the class will work; just pick the one you like better. Add an attribute called 
#flavors that stores a list of ice cream flavors. Write a method that displays 
#these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def display_flavours(self):
        print("In our restuarant we sell icecream and the icecream has the following flavours")
        for flavor in self.flavors:
            print(f"\t- {flavor}")
my_icecream = IceCreamStand( 'icecream', ['chocolate flavor','banana flavor', 'vanilla flavor'])
print(my_icecream.describe_restaurant())
print(my_icecream.display_flavours())
