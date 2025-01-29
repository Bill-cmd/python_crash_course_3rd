locations = ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']
print(f"Original list: {locations}")
print(locations)

print(f"Sorted list: {sorted(locations)}")
print(f"Original list: {locations}")
print(f"Reversed list: {sorted(locations, reverse=True)}")
print(f"Original list: {locations}")

locations.reverse()
print(f"Reversed list: {locations}")
locations.reverse()
print(f"Reversed list again: {locations}")

locations.sort()
print(f"Sorted list: {locations}")
locations.sort(reverse=True)
print(f"Reversed list: {locations}")

