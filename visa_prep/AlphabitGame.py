s = input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
v = 0
c = 0
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] in vowels:
            v += 1
        else:
            c += 1
print("{0},{1}".format(v,c))
