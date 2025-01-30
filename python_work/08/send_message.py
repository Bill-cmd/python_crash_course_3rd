def show_messages(messages):
    print("The messages are:")
    for message in messages:
        print(f"\t{message}")
    
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"The current message is {current_message}")
        sent_messages.append(current_message)

messages = ['message1', 'message2', 'message3']
sent_messages = []

send_messages(messages, sent_messages)

show_messages(messages=messages)
show_messages(sent_messages)