def divide_by(number):
   try:
        return 42 / number
   except ZeroDivisionError:
       print("Error invalid divisor")

print(divide_by(0))
