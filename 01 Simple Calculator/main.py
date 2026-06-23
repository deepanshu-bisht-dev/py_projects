try:
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))

    print('''What kind of operation do you want to perform?\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division''')
    
    o = input("Enter operation")

    match o:
        case "+":
            print(f"The result is {a+b}.")
        case "-":
            print(f"The result is {a-b}.")
        case "*":
            print(f"The result is {a*b}.")
        case "/":
            print(f"The result is {a/b}.")
        case default:
            print(f"No valid value entered.")
except Exception as e:
    print("Enter valid value")
          