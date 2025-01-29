guests = ["Alice", "Bob", "Charlie"]
print(guests)

#absent_guest = "Bob"
#print(f"{absent_guest} can't make it to the party.")
#guests.remove(absent_guest)
#print(guests)

guests.insert(0, "David")
guests.insert(2, "Eve")
guests.append("Frank")
print(guests)

for guest in guests:
    print(f"Hello, {guest}! You're invited to the party.")

print(f"len(guests) = {len(guests)}")

