import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if(level > 0 and level <= 3):
                return level


def generate_integer(level):
    i = 0
    while(i < 10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        try:
            n = int(input(f"{x} + {y} = "))
        except ValueError:
            return False
        else:
            if(n == x + y):
                return True
            else:
                return False

        i += 1



if __name__ == "__main__":
    main()