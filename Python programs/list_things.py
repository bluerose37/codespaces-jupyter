favorites =[]
while True:
    item = input("Add your favorite thing (or type 'done' to finish):")
    if item == 'done':
        break
    favorites.append(item)

print("\nyour favorites:")
for thing in favorites:
    print(f"-{thing}")
