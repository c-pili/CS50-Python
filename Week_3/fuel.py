while True:
    fraction = input("Fraction: ")

    try:
        x, z = fraction.split("/")
        fraction = int((int(x)/int(z))*100)
        if(float(x) <= 0 or fraction > 100):
            x = 0

        else:
            if(fraction == 100):
                print("F")

            elif(fraction == 0):
                print("E")

            else:
                print(fraction,"%", sep="")

            break

    except (ValueError, ZeroDivisionError):
        fraction = "0"