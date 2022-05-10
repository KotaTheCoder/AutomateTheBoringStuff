def area_less_than_hundred(height, width):
    if height * width < 100:
        return True
    else:
        return False



print("20 x 30 square if less than 100 square units:" + str(area_less_than_hundred(20,30)))
