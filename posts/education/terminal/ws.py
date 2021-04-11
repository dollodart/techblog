str1 = "a\t2"
str2 = r"a\t2"

str1 = [bin(ord(x))[2:] for x in str1]
str2 = [bin(ord(x))[2:] for x in str2]

# zero pad
str1 = ['0'*(8-len(x)) + x for x in str1]
str2 = ['0'*(8-len(x)) + x for x in str2]

print(" ".join(str1))
print(" ".join(str2))


