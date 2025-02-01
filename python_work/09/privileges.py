class User:
    # 初始化方法，用于创建类的实例
    def __init__(self, first_name, last_name):
        # 将传入的first_name参数赋值给实例变量self.first_name
        self.first_name = first_name
        # 将传入的last_name参数赋值给实例变量self.last_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name is {self.first_name.title()}, the last name is {self.last_name.title()}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

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

user1 = Admin("Natasha", "Donald")
user1.privileges.show_privileges()