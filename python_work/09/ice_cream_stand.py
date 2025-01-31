class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}, the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is opening now.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Matcha', 'Cream']

    def show_flavors(self):
        print("The flavors:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")

ice_cream1 = IceCreamStand("McDonald", "Xi Can")
ice_cream1.show_flavors()

