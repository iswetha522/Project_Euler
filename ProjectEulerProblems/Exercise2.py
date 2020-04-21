items = [1,2,4543,0,-1]
# new_list = []
# for item in items:
#     new_list.append(item)
#     print(new_list.sort())
smallest = items[0]
largest = items[0]
for item in items:
    if smallest > item:
        smallest = item
    if largest < item:
        largest = item

print(f"Smallest element is {smallest}")
print(f"Largest element is {largest}")


