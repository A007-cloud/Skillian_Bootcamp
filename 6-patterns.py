rows = 4
for i in range(1, rows + 1):  
    for j in range(rows  - i):  
        print(" ", end=" ")
    for k in range(1, i + 1):  
        print("*", end=" ")
    for l in range(i - 1, 0, -1):  
        print("*", end=" ")
    print()