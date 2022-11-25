import random

# x = -10 
#   #True

# if x > 0: 
#   print("broj x je pozitivan")

# if x < 0:
#   print("broj x je negativan")

# vozilo_u_pokretu = True
# brzina = 66

# if vozilo_u_pokretu:
#   print("vozilo se krece")
#   print("proverite i brzinu")
#   if brzina > 50:
#     print("prekoracena brzina")
#   print("ovo izvrsavam kolika god da je brzina")
#   if brzina <= 50:
#     print("brzina je u redu")

# 1 prikaz ; 2 kupovina; 3 izlaz
# proizvod = "duks"
# cena = 3000

# komanda = int(input("unesite komandu:"))

# if komanda == 1:
#   print("Prikazi proizvode")
#   print("Proizvod: ", proizvod, "Cena:", cena)
# if komanda == 2:
#   print("kupovina")
#   stanje = int(input("unesite stanje na racunu: "))

#   if stanje >= cena:
#     print("uspesna kupovina")
#   if stanje < cena:
#     print("neuspesna kupovina")
# if komanda == 3:
#   print("izlaz")  

# broj = 5
# if broj > 0:
#   print("broj je veci od nule")
# else:
#   print("broj je manji ili jednak nuli")


# marija = False
# ksenija = True
# katarina = False

# devojka_na_dejtu = ""

# if marija:
#   devojka_na_dejtu = "marija"
# elif ksenija:
#   devojka_na_dejtu = "ksenija"
# elif katarina:
#   devojka_na_dejtu = "katarina"
# else:
#   devojka_na_dejtu = "una"

# print("izlazi sa mnom: ", devojka_na_dejtu)

# automobil_ponovan = False
# godiste = 2021
# boja = "crna"

# if (automobil_ponovan == True or godiste > 2017) and boja == "crna":
#   print("Kupujem")

# if not automobil_ponovan:
#   print("automobil je polovan")


# prisutan = False #nije na casu
# smer = "python"

# if prisutan == True and smer == "python":
#   print("polaznik je bio na casu")


# if prisutan:
#   print("na casu je")

# if not prisutan: #ako nas interesuje da li je false
#   print("nije na casu")

# trenutni_rezultat = random.randint(1, 100)
# novi_rezultat = int(input("Unesite novi broj(od 1 do 100):"))

# if novi_rezultat > 100 or novi_rezultat < 1:
#   print("Proverite broj, dozvoljeno od 1 do 100")
# else:
#   if trenutni_rezultat < novi_rezultat:
#     print("pobedili ste")
#   elif trenutni_rezultat == novi_rezultat:
#     print("identicne vrednosti!")
#   else:
#     print("izgubili ste")

pol = input("unesite pol: ")
poruka = ""
if pol == "m":
  poruka = "Hey mister!"

else:
  poruka = "Hey miss!"
print(poruka)
poruka = "Hey mister!" if pol == "m" else "Hey miss!"
