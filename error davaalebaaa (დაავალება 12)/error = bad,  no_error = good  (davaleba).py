#1 daivai mas tqven tqvit rom damoukidebeli unda vkofilikavi amitom no more ai da yvelafers me davwer chemi azrovnebit
while True:
    try:
        a = int(input("bizi sheiyvane ricxvi: "))
        b = int(input("bizi sheiyvane MEORE ricxvi: "))

        result_1 = a / b
        print(result_1)
        break
    except (ValueError, ZeroDivisionError):
        print("aqane brat value erroria magas ar gagitareb")
#ez pizi lemon sqvizi

#2
def settings(g, d):
    try:
        e = g / d
        return e
    except ZeroDivisionError:
        print("yo broda nolze rato yof you stupidd")
    except TypeError:
        print("shen giji xuaraxar")

print(settings(28, 12))
print(settings(28, 0))
print(settings(28, "12"))

#3
try:
    e = ["qababi", "shaurma", "nayini", "kartoshka"]
    print(e[4])
except IndexError:
    print("macivarshi meti sawmeli agaraa")

#ddddddd es mommewona

#4
try:
    file1 = open("myresult.txt", "r")
except FileNotFoundError:
    print("ras kitxulob zmao ibuprofeni an paracetamoli dalie iqneb gishvelos")

#5
from math import *

a1 = 28
b1 = 12
c = 10

amosaxsneli = a1x2+b1x+c=0

diskriminanti = b1-4*a1*c

fesvi1 = -a1+diskriminanti.sqrt() / 784
fesvi2 = -a1-diskriminanti.sqrt() / 784
#auuu vnebdebi arzrze ar var ras vaketeb ver mivxvdi davvalebis azrs ra unda gavaketot mtliani diskriminanti davwere mcdelobashi erti ori qula momimatet plssssssss

#6
try:
    v = int(input("bizi sheiyvane ricxvi: "))
    z = int(input("bizi sheiyvane meore ricxvi: "))
    t = int(input("bizi sheiyvane mesame ricxvi: "))

    if v + z > t and v + t > z and t + z > v:
        aritmetikuli = (z + v + t) / 3
        print("oooooo eger aritmetikuli = ", aritmetikuli)
    else:
        raise ValueError("she maimuno egi samkutxedis gverdebi arrr aris")
except ValueError as e:
    print("eeee shecdoma daficsirda eeee: ", e) #robotis xmebi

#karoche mas es aris chemit dawerili kodi nu chemit ise vambob exla davalebebs ai-t vaketebdi adre mara exla aranairi ai prosta me da chemi tvini exla ai-s saqmes tqven gaaketebt da nnomer 5 amixsnit rom moval an ara ar moval xutshabats tamashimaq lol









