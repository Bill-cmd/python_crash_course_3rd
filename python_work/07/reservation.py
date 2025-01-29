while True:
    users = input("How many people will have lunch? ")
    try:
        users = int(users)

        if users > 8:
            print("There has not the free table!")
        else:
            print("There has the free table!")
        break
    except ValueError:
        print(f"{users} is not a number!")
