time = input("What's time is it? ")

heures, minutes = time.split(":")

if((int(heures) == 7) and (int(minutes) <= 30)):
    print("breakfast time ")

elif((int(heures) == 12) and (int(minutes) == 42)):
    print("lunch time")

elif((int(heures) == 18) and (int(minutes) == 32)):
    print("dinner time")