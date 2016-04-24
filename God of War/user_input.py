def main():
    x = input("Enter a number:")
    listName = [5, 4, 3, 2, 8]
    a = getData(listName)
    count = 0
    max = a[0]
    while (i <len(a)-1):
        count = i+1
        if a[i] > max:
            print ("The maximum number in the list is", max)
    def getData(n):
        numbers = [5, 4, 3, 2, 1]
        for x in range(n):
            print ("Enter value", x, ":",)
            value = input()
            numbers.append(value)
        return numbers

validinput = False
while(validinput == False):
        try:
            min = float(input("Please enter a low number:"))
            max = float(input("Please enter a high number:"))
            validinput = True
            for i in range (10):
                if not (i%1):
                    print(i)
                print("The maximum number in the list", i, ":", max)
                print("The minimum number in the list", i, ":", min)

        except:
            print("Sorry the maximum number is 5")
            print("Invalid input")
            print("You must inter a valid integer")
            print("Number must be between 0, and 5", end='\n')

main()