from asyncio.windows_events import NULL

while True:
    fraction = input("Fraction: ")

    try:
        x, z = fraction.split("/")
        fraction = int((int(x)/int(z))*100)
        if(fraction == 100):
            print("F")

        elif(fraction == 0):
            print("E")

        else:
            print(fraction,"%", sep="")

        break

    except ValueError:
        fraction = NULL