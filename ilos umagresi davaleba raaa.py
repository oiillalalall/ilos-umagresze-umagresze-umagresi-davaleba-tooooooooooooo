#1
ilo_tilo = open("numbergamburger.txt", "r") #es ra ritmaa numbergamburger yessss
line = ilo_tilo.readlines()
ilo_tilo.close()

ilo_tilo2 = open("number²", "w")

for n in line:
    numberes = int(n)
    ilo_tilo2.write(str(numberes ** 2) + "\n")

ilo_tilo2.close()

#2
inputt = input("bratich sheiyvane zmao weli: ")
found = False

filee = open("oscars.txt", "r")

for line1 in filee:
    data = line1.split(",")
    year = data[0]
    name = data[3]
    if year == inputt:
        print(name)
        found = True  #ai tipma damiwera mtlianad tab tab ttab tab ttab tab tab da egaa l;maoo

filee.close()

if found == False:
    print("zmobilooo xom kargada xaarrr reebsa wera ha?") #barem debilma vinmem ro daweros ar gayaros errorebi

#3
file = open("oscars.txt", "r")

yvelaze_uncrosi = 167
uncrosis_saxeli = ""

for line in file:
    data = line.split(",")

    age = int(data[2])
    name = data[3]
    if age < yvelaze_uncrosi:
        uncrosis_saxeli = name
        yvelaze_uncrosi = age

file.close()

print("YVELAZEEE UNCROSII OSKAROSANII ARIIISSS:")
print(uncrosis_saxeli, "romelic", yvelaze_uncrosi, "wlisaaa") #au ez pizi lemon scvizi iko ngl es xoda exla github noooooooooooooooooo


