size = int(input("Enter the size of the pattern:"))
i = 0
while i<size:
    i=i+1
    for j in range(1,size+1):
        print("*", end="")
    print("\n")