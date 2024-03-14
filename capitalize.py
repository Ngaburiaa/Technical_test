name = input("Enter your name  ")
namelist = []
capital = name.capitalize()

for i in range(len(capital)):
    if capital[i - 1].isspace():
        namelist.append(capital[i].capitalize())
    else:
        namelist.append(capital[i])
print("".join(namelist))
