cat_names = []
while True:
    name = input("Input a cat name, or enter nothing to stop: ")

    if name == "":
        break

    cat_names = cat_names + [name]

print("The cat names are:\n")

for name in cat_names:
    print(name)
