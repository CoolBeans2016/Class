import math

a = 0
b = 0
c = 0
x = 0

def main():
    print("Please enter the value of a,b,c and x at the following prompts")

    getquadratic()
    display_quadratic()

def getquadratic():

    global a,b,c,x
    a = float(input("Please enter coefficient a: "))
    b = float(input("Please enter coefficient b: "))
    c = float(input("Please enter coefficient c: "))
    x = float(input("Please enter coefficient x: "))

def display_quadratic():
    print("The following quadratics were entered:" ,end="")
    if (b >= 0 and c >= 0):
        print(str(a) + 'x^2 +' + str(b) + 'x+' + str(c))
    elif (b < 0 and c >= 0):
        print(str(a) + 'x^2' + str(b) + 'x+' + str(c))
    elif (b < 0 and c < 0):
        print(str(a) + 'x^2' + str(b) + 'x' + str(c))
    elif (b > 0 and c < 0):
        print(str(a) + 'x^2 + ' + str(b) + 'x' + str(c))
    print('The value of the quadratic is ', calculatequad())


def calculatequad():
    global a, b, c, x
    return( a * x ** 2 + b * x + c)
main()
