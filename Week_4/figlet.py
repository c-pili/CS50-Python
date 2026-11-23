from pyfiglet import Figlet
import sys

def Main():
    try:
        if(len(sys.argv) == 1):
            font = 0
        elif(len(sys.argv) == 3):
            font = sys.argv[1]
            name = sys.argv[2]
        else:
            print("Invalid usage")
            sys.exit(1)

    except IndexError:
        print("Invalid usage")
        sys.exit(1)

    else:
        text = input("Input: ")
        figlet = Figlet()
        if(len(sys.argv) == 1):
            #Figlet.setFont(font=f)
            print(figlet.renderText(text))
            return

        else:
            try:
                f = Figlet(font=name)
                print(f.renderText(text))
                return
            except:
                print("Invalid usage")
                sys.exit(1)

Main()