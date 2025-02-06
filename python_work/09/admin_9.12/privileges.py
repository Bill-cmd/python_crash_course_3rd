from users import User

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("This user has below privilege:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
'''
user1 = Admin("Natasha", "Donald")
user1.privileges.show_privileges()
'''