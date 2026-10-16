input = input("Input: ")

n = input.split()
print(n)
print(n[0])

for i in n:
    if(n[i] == "Twitter"):
        n[i] = "Twwtr"