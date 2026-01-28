#1
faili1 = open("clients.txt", "r")
faili2 = open("espanelebi da germanelebi.txt", "w")

for line in faili1:
    data = line.strip().split(";")
    name = data[0]
    country = data[2]

    if country == "Spain" or country == "Germany":
        faili2.write(name + "\n")

faili1.close()
faili2.close()
#ok ok nice nice ez mara iseti debilivar faili1 "clients ragaca.py" dawere da errorebs ro migdebda ver vxvdebodi da zlivs gavaanalize ro py mqonda da ara txt

#2
emailebi_2011 = []

faili3 = open("clients.txt", "r")

for line1 in faili3:
    data = line1.strip().split(";")
    email = data[1]
    birth = data[3]
    year = birth.split("/")[-1]
    if year == "2011":
        emailebi_2011.append(email)

print(emailebi_2011)

#auuu rac me amas vecaliche wlebi ver davamtxvie imena [] es gamowonda metqi ratom

#3  (zlis mivxvdii ra igulismet qartuli 10000% var dd)
countries = []

faili4 = open("clients.txt", "r")

for line in faili4:
    data = line.strip().split(";")

    country = data[2]

    if country not in countries:
        countries.append(country)

print(countries)
#aqac bevri errorebi gadmomishala gavaswore imitom rom masteer killer pro playere var


