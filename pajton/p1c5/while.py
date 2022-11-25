import random
sekunde = 10

# while sekunde > 0:
#       print(sekunde)
#       sekunde -= 1

# while True:
#       print("cao")



baterija = 90

while baterija > 0:
      print("mozes koristiti telefon", baterija, "%" )
      baterija -= random.randint(5, 20)

for broj in range(11):
      if broj == 5:
            break
      print(broj)


for broj in range(11):
      if broj == 2:
            continue
      print(broj)