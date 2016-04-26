def main():
    a = [8, 4, 9, 3, 7]
    print("Before sort: ", a)
    for j in range(len(a)):
        i = 0
    for k in range(len(a) -1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            i = i+1
    print("After sort: ", a)
    count = 0
    maxNum = a[0]
    minNum = a[0]
    print(i, " ", maxNum)

    while i < len(a)-1:
        i=i+1
        count=count+1
        if a[i] > maxNum:
            maxNum = a[i]
        print (i, " ", maxNum)
    if a[i] < minNum:
        minNum = a[i]
    print("The minimum number in the list is", maxNum)
    print("The minimum number in the list is", minNum)

main()
