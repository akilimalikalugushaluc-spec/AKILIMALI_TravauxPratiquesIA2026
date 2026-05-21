import numpy as np
# 1 operation de calcul de base
def addition(a, b):
    return a + b
def soustration(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("division par zeros est impossible")
    return a / b
# demonstration
print("calcul de base")
print(f"5+3={addition(5, 3)}")
print(f"5/4={division(5, 4)}")
print(f"7-2={soustraction(7, 2)}")
print(f"4*3={multiplication(4, 3)}")   

# 2 CALCUL DES VECTEURS
def addition_vecteurs(v1, v2):
    if len(v1)!=len(v2):
       raise ValueError("les vecteurs doivent avoir la meme taille.")
  # addition les elements indice par indice
    return [v1[i]+v2[i] for i in range(len(v1))]
def produit_scalaire(v1, v2):
    if len(v1) != len(v2):
       raise ValueError("les vecteurs doivent avoir la meme taille.")
 # somme des produits des elements correspondants
    return sum(v1[i]*v2[i] for i in range(len(v1)))
# EXEMPLES
vec1 = [2, 4, 3]
vec2 = [7, 5, 1]
print("somme vecteurs:",addition_vecteurs(vec1, vec2)) #[9,9,4]
print("produit scalaire:",produit_scalaire(vec1, vec2)) # 2*7+4*5*+3*1=37
 
# 3 CALCUL ENTRES MATRICES
def somme_matrices(M1, M2):
    # verification des dimensions
    if len(M1)!=len(M2) or len(M1[0])!= len(M2[0]):
       raise ValueError("les matrices doivent avoir les meme dimensions.")
    nb_lignes=len(M1)
    nb_colonnes=len(M1[0])
# creation de la matrice resutante
resultat=[]
for i in range(nb_lignes):
    ligne=[M1[i][j]+M2[i][j] for j in range(nb_colonnes)]
    resultat.append(ligne)   
print("resultat")
def produit_matrices(M1, M2):
# le nombre de colonnes de M1 doit etre egal au nombre dde ligne de M2
   if len(M1[0])!=len(M2):
      raise ValueError("dimensions incompatibles pour la multiplication de matrices.")
   nb_lignes_M1=len(M1)
   nb_colonnes_M1=len(M1[0])
   nb_colonnes_M2=len(M2[0])

# initiation de la matrice avec zeros
   resultat= [[0 for _ in range(nb_colonnes_M2)] for _ in range(nb_ligne_M1)]
# calcul du produit matriciel
   for i in range(nb_ligne_M1):
       for j in range(nb_colonnes_M2):
           for k in range(nb_colonnes_M1):
               resultat[i][j]+=M1[i][k]*M2[k][j]
   return resultat
# EXEMPLES

mat1=[[1,2],[3,4]]
mat2=[[2,0],[1,2]]
print("somme matrices:",addition_matrices(mat1, mat2))
print("produit matrices:",produit_matrices(mat1, mat2))
