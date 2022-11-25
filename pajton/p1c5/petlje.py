# # x                                 x
# pozicija_automobila = 0
# pozicija_cilja = 10 

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

for ime in ["marko", "milos", "marija", "ana", "sofija"]:
      print("Hello", ime)

print("prva sledeca linija..")

for broj in [1, 2, 3, 4, 5, 6, 7]:
      print("ovo je broj: ", broj)


for broj in range(5, 10, 2):
      print("stampanje broja: ", broj)

for broj in range(100, 0, -1):
      print("Prikaz: ", broj)


pozicija_automobila = 0
pozicija_cilja = 10 

for kretanje in range(5):
      pozicija_automobila += 2
      print(pozicija_automobila == pozicija_cilja)

for kretanje in range(pozicija_cilja + 1):
      pozicija_automobila = kretanje
      print(pozicija_automobila == pozicija_cilja)

for years in range(1990, 2004):
      allowed_years = years
      print("allowed years: ", years)

# for zvezda in range(100):
#       print("*", end="")

# print()
# print("1\t2\t3\t")
# print("************************")

# zeljeni_broj = int(input("unesite zeljeni broj: "))
# for brojac in range(1, zeljeni_broj + 1):
#       print(zeljeni_broj * 1, end="\t")
#       print(zeljeni_broj * 2, end="\t")
#       print(zeljeni_broj * 3, end="\n")


# print(1 * 1, end="\t")
# print(1 * 2, end="\t")
# print(1 * 3, end="\n")



# for x in range(5):
#       for y in range(3):
#             print("ovo je x: ", x, "ovo je y", y)



# for zvezdica in range(6):
      
#       print("*", end= " ")

# print()

# for x in range(10):
#       print(x, end=" ")
#       for y in range(10):
#             print("*", end= " ")
#       print()

# for x in range(6):
#       for y in range(6):
#             if x == y:
#                   print("*", end= " ")
#             else:
#                   print("#", end= " ")
#       print()

# for x in range(6):
#       for y in range(6):
#             print("*" if x == y else "#", end= " ")
#       print()

for x in range(10):
      for y in range(10):
            if x == 0 or x == 9 or y == 0 or y == 9:
                  print("#", end= " ")
            else:
                  print(" ", end=" ")            
      print()

            
            


