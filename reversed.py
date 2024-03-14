number = int(input("Enter a number: "))
num = str(number)


if num[0] == "-":
    a = num[::-1]
    b = int("-" + a[:-1])
    print(b)
else:
    print(int(num[::-1]))
