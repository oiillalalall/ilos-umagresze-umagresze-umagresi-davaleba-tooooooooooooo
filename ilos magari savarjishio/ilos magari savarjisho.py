#1

file1 = open("blablabla", "w")
file1.write("gugugaga")

file1.close()

#2
file2 = open("bubliki123", "r")
blablba = file2.read()
blelllell = len(blablba)

print(blablba)
print(blelllell)


#3
file1 = open("blablabla", "a")
guguggaga = file1.write("gugugaga123")

#4
file2 = open("bubliki123", "r", encoding="utf-8")
b1 = file2.read()

file3 = open("axalaxalaxal", "w", encoding="utf-8")

file3.write(b1)

#5
file1 = open("blablabla", "r")
a1 = file1.read()

file2 = open("bubliki123", "r")
a2 = file2.read()

file4 = open("kideaxali", "w")
file4.write(a1)
file4.write(a2)

#6
file1 = open("blablabla", "r")
h1 = file1.read()

print(h1.upper())

#7
file1 = open("blablabla", "w")
while True:
    texti = input("bro bro sheiyvane bro: ")
    if texti == 0:
        break
    file1.write(texti + "\n")

#8 DRO AR MEKOO :((((((((((((((




