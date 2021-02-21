liste = [21, 47, -12, 74, 5, 28, 33]
liste.sort()
max=0               
for i in range (0,len(liste )-1):
    if liste [i+1]>liste [i]:
        max=liste [i+1]
print ("le plus grand element est:", max)
