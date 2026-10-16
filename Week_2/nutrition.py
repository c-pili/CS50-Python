item = input("Item: ").lower()

print("Calories: ", end="")
match item:
    case "apple":
        print("130")

    case "avocado":
        print("50")

    case "Sweet Cherries":
        print("100")