from asyncio.windows_events import NULL

while True:
    date = input("Date: ")

    try:
        j, m, a = date.split("/")
        if(j>30 or m>12):


        else:
            print(j, m, a, sep="-")

    except ValueError:
        m, j, a = date.split(" ")
        if(j>30 or m>12):


        else:
            print(j, m, a, sep="-")