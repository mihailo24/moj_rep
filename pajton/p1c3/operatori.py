import random

kurs = "Python Fundamentals"
print(kurs)

a = 10
b = 5

print(a + b)

rezultat_sabiranja = a + b
print(rezultat_sabiranja)

print("Oduzimanje:", a - b)
print("Mnozenje:", a * b)
print("Deljlenje + int:", int(a / b))
print("Deljlenje:", a / b)



print("Celobrojno deljenje:", a // b)
print(10 // 3)
print(10 / 3)

print(a ** 2) # a * a
print(a ** 3) # a * a * a

# 10 / 3 = 3
#3*3 = 9
#9 + 1 = 10

print(10 % 3) #MODULO
print(5 % 2)
print(4 % 2)
print(8 % 2)

print(-a)
#a = -a
print(a)

godine = 25
#godine + 1

godine = godine + 1

godine += 1

print(godine)


godine -= 5
print(godine)

godine *= 2
print(godine)

#godine /= 2
#print(godine)

godine //= 2
print(godine)

# a = 5
# b = 3
# x = a + b
# print(x)

# broj1 = int(input("Unesite prvi broj: "))
# print(broj1)

# broj2 = int(input("Unesite drugi broj: "))
# print(broj2)

# print("Rezultat je: ", broj1 + broj2)

# poluprecnik = float(input("Unesite poluprecnik: "))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi
# print("Povrsina kruga je: ", povrsina)

# unos = input("Unesi nesto: ")

# print(unos.isnumeric())

stara_kilaza = 80
nova_kilaza = 99

print(stara_kilaza > nova_kilaza)
print(stara_kilaza < nova_kilaza)

print(nova_kilaza == 100)
print(nova_kilaza != 100) # != razlicito

print(stara_kilaza >= 80)

username = "test"
password = "abc123"

print(username == "test")
print(password == "abc123")


godine = 20 
print(godine >= 16)

# broj = int(input("Unesite broj: "))

# # % modulo

# provera = broj % 2

# print("Paran broj?", provera == 0)

# import random

# korisnik = int(input("Unesite broj: "))
# racunar = random.randint(1, 10)

# print("Korisnik: ", korisnik)
# print("Racunar: ", racunar)
# print("Pogodak: ", korisnik == racunar)



# automobil                               cilj
# 0                                       50

automobil = 0
cilj = 50

print(automobil >= cilj)
automobil += 10
print(automobil >= cilj)

automobil += 20
print(automobil >= cilj)


automobil += 25
print(automobil >= cilj)

provera_imena = True   # ime == sacuvano_ime
provera_sifre = False   # sifra == sucavana_sifra

print(provera_imena and provera_sifre)

''' 
and

true true -> true
true false -> false
false true -> false
false false -> false

or
true true -> true
true false -> true
false true -> true
false false -> false
'''

lepo_vreme = True
print(not lepo_vreme)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

x = 15
y = 15
print(x == y)

#python 2022

kurs = input("Unesite kurs: ")
generacija = int(input("Generacja: "))

odobreno = kurs == "python" and generacija == 2022

print(odobreno)

