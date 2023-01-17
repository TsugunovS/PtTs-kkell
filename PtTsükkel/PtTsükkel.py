from math import * 
from random import * 
#0
positive = 0
negative = 0
while True:
    a=int(input("Sisestage number: "))
    if a>0: positive +=a
    elif a<0: negative +=a
    else:break
print("Positiivne:", positive, "Negatiivne:", negative)




#Ülesanne 9 Pisike korrutustabel
n=int(input("Sisestage number n: "))
for i in range(1,11):
    print(f' {n} * {i} = {n*i} ')
print()

#archi
n=int(input("Дай позитивное число: "))
while True:
    print(n, end=" ")
    n -= 1
    if n<0:
        break

#p
#o=int(input("Sisesta arv: "))
#if o==r:
#    print(f"Sa arvasid et sul läks {n} katset."):
#    break
#elif r>o:
#    print("Väga väike")
#elif o>r:
#    print("Väga suur")
#    n=n+1


#michael
#while True:
#    print("Tere tulemast!")
#    try:
#        print("Latte, 2.50 euro.")
#        print("Espresso, 2 euro.")
#        print("Cappuccino, 3 euro.")
#        print("Kakao, 2.20 euro.")
#        s=float(input("Sisestage summa: ")) # 3.0
#        if s<2 or s>3: break
#        m=input("Valige makseviia: ")
#        if m.lower()=="sularaha":
#            print("anna raha")
#        hind=float(input("Vali hind"))
#        if summa==hind:
#            print("Täname ostu eest")
#        if m.lower()=="kaardiga":
#            n=int(input("Sisestage kaardi number: "))
#            print(n,"selle kaardiga on tehtud makse")
#        elif summa>hind:
#            print(f"Tagasiraha: {hind-s}")
#    except:
#        print("")






#22 artem
print("Ma tahan kommi")
katsed = 0
answer=""
while answer!="komm":
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "komm":
        print(f"Teil kommid kirjutakse kulus {katsed} kaste.")
        break


#0 artem
p=0
while True:
    number = int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")
print("Kasted",p)

#nikita ülesane 11
#print("Arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
#a=randint(1,10)
#vastus=int(input("mis arv on mõistatanud arvutit?:"))
#k=p=1
#while vastus!=a:
#    print("Ära sa ei arvanud ära, proovi uuesti: ")
#    vastus=int(input("Sisesta vastus: "))
#    k+=1
#    p+=1
#    if k>2:
#        print("Püüdlused on lõppenud")
#        b=input("Kas proovi veel kord: ")
#        if b.upper()=="JÄH":
#            k=0
#            continue
#        else:
#            break
#if vastus==a:
#    print("Palju õnne, sa arvasid ära!",p )
#
#print()


#Ёлка
#for i in range(1,5):
#    x=str("*"*i).center(18," ")
#    print(x, end="")
#    print()
#for i in range(1,7):
#    x=str("*"*(1+2)).center(18," ")
#    print(x, end="")
#    print()
#for i in range(1,10):
#    x=str("*"*(i+4)).center(18," ")
#    print(x, end="")
#    print()
   #
#num = 5
#while num <= 50:
#    print("number",num)
#    num += 1

#x=5
#while True: 
#    if x%5==10:
#        print(x, end=" ")
#    x+=1
#    if x==50: break
#print()

#2(6)
#n=0
#print("kolmnurga")
#for e in range (11, 0,-1):
#    n = n + 1
#    for f in range (1, n+1):
#        print("*", end = "")
#    print()
#print("")

#ülesanne 1(6)
#for x in range(S):
#    print("******")

#Ülesanne 9 Pisike korrutustabel

num=int("5")
n=int(input("Sisestage number n: "))
for i in range(1,11):
    print(f' {5} * {i} = {n*i} ')
print()




#=5
#while True:
#    num=("Sisestage number: ")
#    if x%5==11:
#        print("x, end=")
#    if
#else:
print()




