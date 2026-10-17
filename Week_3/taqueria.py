coin = 0
while True:
    try:
        item = input("Item: ").lower()

        match item:
            case "taco":
                coin += 3.00
                print("Total: $", coin, sep="")

            case "baja taco":
                coin += 4.00
                print("Total: $", coin, sep="")

            case "tortilla salad":
                coin += 8.25
                print("Total: $", coin, sep="")

            case "burrito":
                coin += 7.50
                print("Total: $", coin, sep="")

            case "super quesadilla":
                coin += 9.50
                print("Total: $", coin, sep="")

            case "nachos":
                coin += 11.00
                print("Total: $", coin, sep="")

    except EOFError:
        break

