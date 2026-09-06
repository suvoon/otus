for x in range (0, 25):
    for y in range (0, 25):
        if (x >= 16) and (y >= 16):
            print("#", end="")
        else:
            print(".", end="")
    print("")