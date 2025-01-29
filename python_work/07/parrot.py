prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
quit_code = 'quit'
'''
message = ""
while message.lower() != quit_code:
    message = input(prompt)
    if message.lower() != quit_code:
        print(message)

'''

active = True
while active:
    message = input(prompt)

    if message.lower() == quit_code:
        active = False
    else:
        print(message)
