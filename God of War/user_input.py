def main():
    user = input("Enter a number")
    high = max(maxnumber_list)
    low = min(minnumber_list)

    for i in range(high, low):

def maxnumber_list():
    maxnumber_list(9)
    maxnumber_list.append("highest number")
    return maxnumber_list


def minnumber_list():
    minnumber_list(2)
    minnumber_list.append("lowest number")
    return minnumber_list

    print(minnumber_list, maxnumber_list)

main()

