def main():

    validinput=False
    while(validinput==False):
        try:
            a = float(input("Please enter coefficient a: "))
            b = float(input("Please enter coefficient b: "))
            c = float(input("Please enter coefficient c: "))
            x = float(input("Please enter coefficient x: "))
            validinput = True
        except:
           print("Invalid input")

    print("The value of the quadratic is:", a * x ** 2 + b * x + c)
main()