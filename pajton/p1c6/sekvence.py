#            0       1     2      3
osoba = ["Mihailo", 30, "crna", True]
print(osoba)

print("ime:", osoba[0])
print("godine:", osoba[1])

automobili = ["opel", "mercedes", "toyota"]
print(automobili[1])


#       012345
kurs = "python"
print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])
print(kurs[4])
print(kurs[5])



for x in range(6):
      print("Na poziciji: ", x, kurs[x])

# len(sekvenca) - komanda koja prebroji clanove sekvence

duzina = len(kurs)
print(duzina)

# ustanova = "IT academy"

# for indeks in range(len(ustanova)):
#       print(ustanova[indeks])

primer = "zadatak1"


for y in range(len(primer)):
      print(primer[y])

# for y in range(8):
#       print(primer[y])

''' 
while petlja moze ali losije funkcionise

 broj_karaktera = len(primer)
 indeks = 0

 while indeks < broj_karaktera:
       print(primer[indeks])
       indeks += 1 
       
'''

korisnicko_ime = "admin"
uneto_kor_ime = input("Unesi korisnicko ime: ")

if korisnicko_ime == uneto_kor_ime.lower():
      print("dobrodosli")
else:
      print("pogresni podaci")


racunar = "laptop"
model = "macbook"
racunar[1] = "C"
racunar + model
racunar = "desktop"

