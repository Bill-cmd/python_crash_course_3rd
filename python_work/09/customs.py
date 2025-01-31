class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}, the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is opening now.")

    def set_number_served(self, number):
        try:
            self.number_served = number
        except TypeError:
            print(f"{number} is not a number!")

    def increment_number_served(self, number):
        try:
            self.number_served += number
        except TypeError:
            print(f"{number} is not a number!")

restaurant = Restaurant("Quanjude", "Zhong can")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"There is {restaurant.number_served} customs.")
# change the customs
restaurant.number_served = 12
print(f"There is {restaurant.number_served} customs.")

restaurant.increment_number_served(22)
print(f"There is {restaurant.number_served} customs.")