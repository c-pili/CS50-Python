name = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):
    name[i] = input("Name: ")
    print("Adieu, adieu,to ", end="")
    for j in range(i+1):
        if j+1 == i:
            print(name[j], "and", name[j + 1], end="")
            break
        if i == 0:
            print(name[j], end="")
        else:
            print(name[j], end=", ")

    print("")
