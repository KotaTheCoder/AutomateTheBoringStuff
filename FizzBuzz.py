user_number = int(input("Pick a number"))

for i in range(1,user_number+1,1):

    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)






