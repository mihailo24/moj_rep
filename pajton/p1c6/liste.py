osoba = ["Sofija", 25, "plava", False]

for x in range(len(osoba)):
      print(osoba[x])

for osobina in osoba:
      print(osobina)

voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

for stavka in voce_i_povrce:
      print(stavka)

for i in range(len(voce_i_povrce)):
      print("na indeksu: ", i, "nalazi se: ", voce_i_povrce[i])

for indeks, vrednost in enumerate(voce_i_povrce):
      print("indeks: ", indeks, "Stavka: ", vrednost)

automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Opel"]
#Pozicija: 0 Auto: Citroen

# for x in range(len(automobili)):
#       print("Pozicija: ", x, "Auto: ", automobili[x] )

for pozicija, auto in enumerate(automobili):
      if len(auto) == 3:
            print(auto)

automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia Sportage"

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)

broj_opela = 0

for indeks in range(len(automobili)):
      if automobili[indeks] == "Opel":
            print("evo ga opel")
            broj_opela += 1

print("imam ", broj_opela, "na placu.")

automobili.clear()
print(automobili)

prazan_plac = []


automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Peugeot", "Audi"]

automobili_akcija = []

for i in range(len(automobili)):
      if i == 1 or i == 2 or i == 3:
            automobili_akcija.append(automobili[i])

print(automobili_akcija)

automobili_akcija == automobili[1:4:2]
print(automobili_akcija)

a = [3, 7, 1, 9, 2, 4, 5, 12]
parni = []
neparni = []

for x in a:
      if x % 2 == 0:
            parni.append(x)
      else:
            neparni.append(x)
print(parni, neparni)
