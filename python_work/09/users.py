class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name is {self.first_name.title()}, the last name is {self.last_name.title()}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

user1 = User("Natash", "Ole")
user1.describe_user()
user1.greet_user()

