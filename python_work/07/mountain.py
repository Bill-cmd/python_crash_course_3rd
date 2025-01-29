responses = {}
# 设置⼀个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提⽰输⼊被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将回答存储在字典中
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
