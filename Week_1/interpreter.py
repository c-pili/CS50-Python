expression = input("Expressions: ")

x, y, z = expression.split(" ")

match y:
    case "+":
        print(int(x)+int(z))

    case "-":
        print(int(x)-int(z))

    case "*":
        print(int(x)*int(z))

    case "/":
        if(int(z) == 0):
            print("Division by zero")
        else:
            print(int(x)/int(z))
