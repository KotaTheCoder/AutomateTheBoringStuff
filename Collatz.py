def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number +1)
        return 3 * number + 1


collatz(20)

while True:
    try:
        user_number = int(input("Pick a number\n"))
        break
    except ValueError:
        print("Please input a valid integer")

while user_number != 1:
    user_number = collatz(user_number)
