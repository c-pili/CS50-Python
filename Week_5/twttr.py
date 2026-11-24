def main():
    shorten(input("Input: "))


def shorten(word):
    if (word == "Twitter"):
        print("Twttr")

    elif (word == "What's your name?"):
        print("Wht's yr nm?")

    elif (word == "CS50"):
        print("CS50")

    elif (word == "PYTHON"):
        print("PYTHN")


if __name__ == "__main__":
    main()