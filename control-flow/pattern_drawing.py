size = 4
while size <= 0:
    print("Please use a positive integer")
row = 1
while row <= 4:
    for i in range(4):
        print("*", end="")
    print()
    row += 1