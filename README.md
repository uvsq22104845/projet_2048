# projet_2048
#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq22100752/projet_2048
#########################################


def win():
    for x in range(0,4):
    for y in range(0,4):
      if grille[x][y]==2048:
        print("Gagnez!!!")
        game=input("recommencer une partie ? ")
        return(game)

#Permet de fusioner en puissance de 2 les cases de même valeur et situé côte à côte
def fusion(grille):
  for y in range (0,4):    # verifie si deux valeurs côte à côte sont indentiques
    for x in range (0,len(grille[y])-1):
          if grille[y][x]  == grille[y][x+1]:
              grille[y][x+1] = 2*grille[y][x] # La valeur d'un entier est doublée et l'autre est supprimée
              grille[y][x]= 0
  
  return(grille)
