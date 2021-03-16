N=int(input("Donner le nombre d'entier:"))
L1=[]
for i in range (N):
    A=int(input("Donner un entier:"))
    L1.append(A)
print("affichage des nombres de la liste")
print(L1)
LPOS=[]
LNEG=[]
for i in range(N):
    if L1[i]>0:
       LPOS.append(L1[i])
    else:
       LNEG.append(L1[i])
print("affichage des nombres positifs:liste LPOS")
print(LPOS)
print("affichage des nombres negatifs:liste LNEG")
print(LNEG)
