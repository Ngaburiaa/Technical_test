vowel = ["a","e", "i", "o", "u"]
countvowel = []
name = input("Enter the string:  ").lower()
for i in range(len(name)):
    if name[i] in vowel:
        if name[i] not in countvowel:

            countvowel.append(name[i])

print(len(countvowel))
