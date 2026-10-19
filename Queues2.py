from collections import deque

queue = deque(["Alice", "Bob", "Charlie"])
print("Initial Line", list(queue))
#New Arrival
queue.append("David")
queue.append("Aarin is cool")
print("\nServing Customers...\n")

while queue:
    person = queue.popleft()
    print(f'{person} bought a ticket.')

print("\nAll customers have been served.")
