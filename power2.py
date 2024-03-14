n=int(input("Enter your  number:  "))


def power2(n):

    if n / 3 == 1:
        return True


    else:
        if n % 3 == 0:
            n = power2(n / 3)
            return n
        else:
            return False


print(power2(n))
