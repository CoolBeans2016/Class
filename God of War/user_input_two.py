def main():
    x = input("Please enter a number:")
    a = [5, 6, 7, 8, 9]
    print(a)
    b = [5, 6, 7, 8, 9]
    print(b)
    i = 0
    count = 0
    max = a[0]
    min = b[0]
    print(i, " ", max)
    while i < len(a)-1:
        i=i+1
        count=count+1
        if a[i] > max:
            max = a[i]
        print (i, " ", max)
    else:
        print("The maximum number in the list is", max)
    print("The minimum number in the list is", min)

main()



