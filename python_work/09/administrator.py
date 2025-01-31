class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name is {self.first_name.title()}, the last name is {self.last_name.title()}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"{self.first_name.title()} {self.last_name.title()} has below privilege:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

user1 = Admin("Natasha", "Donald")
user1.show_privileges()
