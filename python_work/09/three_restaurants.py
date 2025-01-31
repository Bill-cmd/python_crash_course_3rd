class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}, the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is opening now.")

restaurant = Restaurant("Quanjude", "Zhong can")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Haidilao", "Huo guo")
restaurant2 = Restaurant("Beijing Restaurant", "Zhong can")
restaurant3 = Restaurant("McDonald's", "Xi Can")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
