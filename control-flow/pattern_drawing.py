size = int(input("Enter a positive integer for the size of the pattern:"))
while size <= 0:
    print("Enter a positive integer.")
    size = int(input("Enter a positive integer for the size of the pattern:"))
row = 0
while row < size:
    for i in range(size):
        print("*", end="")
    print()
    row += 1