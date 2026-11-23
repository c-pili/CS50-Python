import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    else:
        if(level > 0 and level <= 10):
            break

n = random.randint(1, level) #randrange aussi

while True:
    while True:
        try:
            number = int(input("Gess: "))
        except ValueError:
            continue
        else:
            if number > 0:
                break
    if number == n:
        print("Just right!")
        break

    elif number > n:
        print("Too large!")

    else:
        print("Too small!")