#Problema 1 - parola

ok = 1
passw = input("Introdu parola: ")
if len(passw) < 10:
    print("Parola este prea scurta!")
    ok=0
else:
    for i in passw:
        if i == ' ':
            print("Parola nu poate contine spatiu (' ')")
            ok=0
            break
if ok == 1:
    print("OK")

#Problema 2 - nr litera in cuvant

cuvant = input("Introdu cuvantul: ")
litera = input("Introdu litera: ")
k=0

for i in cuvant:
    if i ==litera:
        k+=1
print(k)
print()


#Exercitiul 3 - toate puterile lui 3 cuprise intre 200 si 300
i=0
print("Puterile lui 3 cuprinse intre 200 si 300: ")
while 3**i <= 200:
    i+=1
while 3**i < 300:
   print(3**i)
   print()
   i+=1


#Exercitiul 4 - suma nr

numar = int(input("Introdu un numar: "))
suma = 0
for i in range (0,numar+1):
    suma += i
print(f"Suma cu for: {suma}")
suma = 0
while numar > 0:
    suma += numar
    numar-=1
print(f"Suma cu while: {suma}")


#Exercitiul 5 - numaratoare inversa

numar = int(input("Introdu un numar: "))
copie = numar
print("Numerele descrescator cu for: ")
for i in range (numar,-1,-1):
    print(i, end=' ')
print()
print("Numerele descrescatoare cu while: ")
while(numar >= 0):
    print(numar,end = ' ')
    numar-=1