def main():
    value(input("Greeting :").lower())


def value(greeting):
    if (greeting == "What's happening?"):
        print("$100")

    elif (greeting == "How you doing?"):
        print("$20")

    else:
        print("$0")


if __name__ == "__main__":
    main()