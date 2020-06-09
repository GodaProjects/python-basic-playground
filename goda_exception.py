while True:
    try:
        input_from_goda = int(input("Please enter a number"))
        break
    except ValueError:
        print("You did not enter a number")
    except:
        print("Unknown error")

print("Thank you")
