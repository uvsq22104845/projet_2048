#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq22007534/tas_de_sable
#########################################




########################### Blibliothèques #######################################"


import tkinter as tk
import random as r
from functools import partial


########################### PARAMETRE FENETRE + VARIABLE GLOBAL #######################################"

a, b = 850,850

root = tk.Tk()
root.title("tas de sable")
root.geometry("950x900")
canvas = tk.Canvas(root, width = a, height = b,bg="white")
nbcase=16
taillecase=(4*(a//nbcase))
configcourante=[]
configbasique=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
x0=1
y0=1

########################### FONCTIONS #######################################"
configcourante=configbasique

def coloration():
    global colorcarre
    colorcarre=[]
    for i in range (len(configcourante)):
        for j in range (len(configcourante[i])):
            if configcourante[i][j]==0:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#ccc',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==4:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#eee4da',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==8:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#ede0c8',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==16:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#f2b179',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==32:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#f59563',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==64:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#f67c5f',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==128:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#f65e3b',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==256:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#edcf72',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==512:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#edcc61',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==1024:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#edc850',outline='#b7b7b7',width=10))
            elif configcourante[i][j]==2048:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#edc53f',outline='#b7b7b7',width=10))
            else:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill='#edc22e',outline='#b7b7b7',width=10))


def play():
    return

def exit():
    return root.destroy




################################################BOUTONS##################################



playB=tk.Button(root, text ="Play", command=coloration)
playB.grid(row=1,column=0)

exitB=tk.Button(root, text ="Exit", command=root.destroy)
exitB.grid(row=0,column=0)


########################### grid #######################################"
grid1=canvas.grid(row=1,column=1 ,rowspan=6,columnspan=6)


########################### bind #######################################"
canvas.bind()
canvas.bind()
canvas.bind()

########################### MAINLOOP du programme #######################################"
root.mainloop()