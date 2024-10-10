'''ex 8
def valeur_absolue(x):
    if abs(-9):
       return(x)
print (valeur_absolue(9))'''



'''ex 9
def est_entier (x):
    if x==(int):
        return True 
    else:
        return False
print(est_entier(2.5))'''



'''ex 10
def est_pair(n):
    if n%2==0:
        return True
    else :
        return False
print(est_pair(14))'''


'''ex 11
def intervalle1(x):
    if (x> -2) and (x<3):
        return True
    else:
        return False
print(intervalle1(2))'''





'''ex 12
def sign(nombre):
    if nombre > 0:
        return 'positif'
    elif nombre ==0:
        return 'nul'
    else:
        return 'negatif'
print(sign(7))'''


'''ex 13
def est_bissewtile(n):
      if ((n%4==0 and n%100!=0) or (n%400==0)):
            return True
      else:
            return False
print(est_bissewtile(2000))'''



'''ex multi
def nb_pairs(n):
  for k in range (n+1):
    print(100*k)
nb_pairs(10)'''




def suite(n):
    u = 1
    for k in range(n):
      u = 2*u+k
    return u
print(suite(60))
'''L=[]
for k in range(1,101):
  L+= [k]
print (L)'''



'''L=[]
for k in range(1,101):
    L.append(k)
print (L)'''



'''L=[]
L=100*[0]
for k in range(1,101):
    L[k-1]=k
print(L)'''



'''L=[]
for k in range(1,101):
    L=L+[k*2]
print(L)'''



'''def carre(n):
    carre = []
    for k in range(1,n+1):
        carre.append(k**2)
    return carre
print(carre(5))'''




'''def carre_compr(n):
    L=[k*2 for k in range(1,n+1)]
    return L 

print(carre_compr(1000))'''



liste_1=[x for x in range(1,20,2)](liste)
print(liste_1)
liste_2=[x**2 for x in range(11)]
print(liste_2)
    
