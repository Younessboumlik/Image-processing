import matplotlib.pyplot as plt
import numpy as np
from random import randrange
###############PARTIE 1&2 ###############
# Question 1
def AfficherImg(img):
    '''Affiche sur l'ecran une image en argument'''
    plt.axis("off") # Ne pas afficher les axes
    # plt.imshow(img, interpolation="nearest")
    plt.imshow(img, cmap = "gray")#palette predefinie pour afficher une image
    #plt.imshow(img)
    plt.show()
# Question 2
def ouvrirImage(chemin):
    '''Ouvre une image jpg ou bmp on retourne une matrice'''
    img=plt.imread(chemin)
    return img
# Question 3
def saveImage(img):
    '''Sauvgarde une image sous forme jpg ou bmp'''
    plt.imsave("image1.png",img)
# Question 4
def image_noire(h, l):
    '''Cree une image noire de hauteur h et de largeur l'''
    M=np.array([[0]*l for i in range(h)],dtype=int) #matrice nulle de taille h*l 
    return M
# Question 5
def image_blanche(h, l):
    '''Cree une image blanche de hauteur h et de largeur l'''
    M=np.array([[1]*l for i in range(h)],dtype=int) #matrice initialisee par les 1, de taille h*l
    return M
# Question 6
def creerImgBlancNoir(h,l):
    '''Cree une image en noir & blanc de hauteur h et de largeur l'''
    M=np.array([[0]*l for i in range(h)],dtype=int) #matrice nulle de taille h*l
    for i in range(h):
        for j in range(l):
            M[i][j]=(i+j)%2 # Chaque element de M reçoit le reste de la division euclidienne 
                             # de sa position (i+j)
    return M
# Question 7
def negatif(Img):
    '''Construit le negatif de l'image Img par permutation entre les 0 & 1'''
    n=len(Img) # nbr de lignes de la matrice Img
    p=len(Img[0]) # nbr de colonnes de la matrice Img
    for i in range(n):
        for j in range(p):
            if Img[i][j]==0:# condition sur le contenue des elements de Img
               Img[i][j]=1  # si il egale a 0 sera remplace par 1,vice-versa
            else:
                Img[i][j]=0
    return Img
# Question 8 les tests    ;;;;
###############PARTIE 3 ###############
# Question 9
def luminance(Img):
    '''Calcule la brillance de Img ;la moyenne des pixels'''
    n=len(Img) # nbr de lignes de la matrice Img
    p=len(Img[0]) # nbr de colonnes de la matrice Img
    s=0
    for i in range(n):
        for j in range(p):   
            s+=Img[i][j] # La sommation du contenu de tous les éléments de la Img
    if n!=0 and p!=0:
        return s/(n*p) # on divise la somme sur le nbr des elmts pour avoir la moyenne
# Question 10
def constrast(Img):
    '''Calcule la variance des niveaux de gris de Img'''
    n=len(Img) # nbr de lignes de la matrice Img
    p=len(Img[0]) # nbr de colonnes de la matrice Img
    var=0
    for i in range(n):
        for j in range(p):   
            var+=((Img[i][j]- luminance(Img))**2)/(n*p) # formule de la variance
    return var
# Question 11
def profondeur(Img):
    '''Renvoie la valeur maximale d'un pixel de Img'''
    n=len(Img) # nbr de lignes de la matrice Img
    p=len(Img[0]) # nbr de colonnes de la matrice Img
    max=Img[0][0]
    for i in range(n):
        for j in range(p):
            if Img[i][j]>max: # condition sur le contenue des elements de Img
                max=Img[i][j] # la variable max reçoit le contenu de l'élément de la matrice qui convient
    return max
# Question 12
def Ouvrir():
    '''Renvoie l'Image A a partir de son chemin predifini'''
    Img=ouvrirImage("C:/Users/hp/Desktop/MiniProjet/image A.jpg")
    # en utilisant l'ouverture a partir de son repertoire
    # ce chemin doit etre change chaque fois on change l'emplacememt d'Image A 
    return  Img
# Question 13
def inverser(img):
    '''Renvoie l'inverse d'une image en argument'''
    n=len(img) # nbr de lignes de la matrice img
    p=len(img[0]) # nbr de colonnes de la matrice img
    M=[[0]*p for i in range(n)] # matrice nulle de taille n*p
    for i in range(n):
        for j in range(p): # pour chaque pixel x le niveau de gris oppose, le blanc devient
                           # noir et vice-versa
            M[i][j]=255-img[i][j] 
    return M
# Question 14
def flipH(img) :
    '''Renverse l'image en argumet par la symetrie d'axe vertical passant par son milieu'''
    n=len(img) # nbr de lignes de la matrice img
    p=len(img[0]) # nbr de colonnes de la matrice img
    M=[[0]*p for i in range(n)]
    for i in range(n):
        for j in range(p): 
            M[i][j]=img[i][p-1-j]# chaque elmt de M contient son symetrique dans img par 
                                 # rapport l'axe vertical qui passe par le milieu de img
    return M
M=[[[12,55,12],[15,15,15],[34,34,34],[45,45,45]],[[14,14,14],[15,15,15],[35,35,35],[44,44,44]]]
# Question 15
def poserV(img1,img2) :
    '''Ses argumets(image1,image2) de meme taille, renvoie l'image obtenue en posant img1 sur img2'''
    n=len(img1) # nbr de lignes de la matrice img1
    p=len(img1[0]) # nbr de colonnes de la matrice img1  
    M=[[0]*p for i in range(2*n)] # matrice nulle de taille 2n*p
    for i in range(2*n):
        for j in range(p): 
            if i<n: # (n-1)est la derniere ligne de img1
                M[i][j]=img1[i][j]
            else:  # (n)est la premiere ligne pour img2
                M[i][j]=img2[i-n][j]
    return M
# Question 16
def poserH(img1, img2):
    '''Ses argumets(image1,image2) de meme taille, renvoie l'image obtenue en posant img2 a dtoite de img2'''
    n=len(img1) # nbr de lignes de la matrice img1
    p=len(img1[0]) # nbr de colonnes de la matrice img1  
    M=[[0]*2*p for i in range(n)] # matrice nulle de taille n*(2p)
    for i in range(n):
        for j in range(2*p): 
            if j<p: # (p-1)est la derniere colonne de img1
                M[i][j]=img1[i][j]
            else:  # (p)est la premiere colonne pour img2
                M[i][j]=img2[i][j-p]
    return M
M=[[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]],
[[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]],
[[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]]]
# Question 22
         # print(M[0][1][1]) # le resultat :50
         # print(M[1][0][1]) # le resultat :255
         # print(M[2][1][0]) # le resultat :255
# Question 23
         # Dans une image RGB chaque pixel est represente par 3 octets d'ou la 
         #  memoire necessaire est de (3*n*p)octets ou encore(3*n*p*8)bits. 
def taille(img):
            return 3*len(img)*len(img[0])
# Question 24
def initImageRGB(imageRGB):
    '''Initialise aleatoirement et renvoie un tableau imageRGB a 3 dimension'''
    n=len(imageRGB) # nbr de lignes de la matrice imgageRGB
    m=len(imageRGB[0]) # nbr de colonnes de la matrice imgageRGB
    tab=[[[0]*3 for i in range(m)] for j in range(n)] # matrice nulle de taille 3*n*m
    for i in range(n):
        for j in range(m):
            for k in range(3):
                tab[i][j][k]=randrange(0,256) # un nombre aleatoire entre 0 & 256
    return tab
# Question 25
def symetrieH(img):
    '''prend une image en argument et renvoie sa symetrique par rapport a l'axe horizontal'''
    n=len(img) # nbr de lignes de la matrice img
    m=len(img[0]) # nbr de colonnes de la matrice img
    M=[[[0]*3 for i in range(m)] for j in range(n)] # matrice nulle de taille 3*n*m
    for i in range(n):
        for j in range(m): 
            for k in range(3):
                M[i][j][k]=img[i][m-1-j][k]  #d'une maniere inverse on stocke selon les colonnes de img dans M  
    return M
def symetrieV(img):
    '''prend une image en argument et renvoie sa symetrique par rapport a l'axe vertical'''
    n=len(img) # nbr de lignes de la matrice img
    m=len(img[0]) # nbr de colonnes de la matrice img
    M=[[[0]*3 for i in range(m)] for j in range(n)] # matrice nulle de taille 3*n*m
    for i in range(n):
        for j in range(m): 
            for k in range(3):
                M[i][j][k]=img[n-1-i][j][k] #d'une maniere inverse on stocke selon les lignes de img dans M
    return M
# Question 26
def grayscale(imageRGB):
    '''prend en argument une imageRGB et renvoie une image en niveaux de gris de taille n*m'''
    n=len(imageRGB) # nbr de lignes de la matrice imageRGB
    m=len(imageRGB[0]) # nbr de colonnes de la matrice imageRGB
    M=[[0]*m for i in range(n)] # matrice nulle de taille n*m
    for i in range(n):
        for j in range(m): 
                M[i][j]=(min(imageRGB[i][j])+max(imageRGB[i][j]))//2  # les elmts de M sont la moyenne entre 
                                                                      #et le min de chaque pixel
    return M
