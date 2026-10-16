expression = input("Expressions: ")

x, y, z = expression.split(" ")

match y:
    case "+":
        print(float(x)+float(z))

    case "-":
        print(float(x)-float(z))

    case "*":
        print(float(x)*float(z))

    case "/":
        if(int(z) == 0):
            print("Division by zero")
        else:
            print(float(x)/float(z))
