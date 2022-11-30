# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 02:01:16 2022

@author: guill
"""

######################################################
#import fonction externe
import csv
######################################################

def lecture_donne(Doc): #Lecture donner tab
       # ouverture en lecture du fichier csv
    with open(Doc, newline='',encoding="utf-8") as fichier:
            # on crée un objet reader
        lecture = csv.reader(fichier, delimiter=',')
        tab=[]
        # lecture et affichage des lignes:
        for ligne in lecture:
            tab.append(ligne)
    return tab

def trombifr(tab):
    print("				<div class=&carte&>")
    print("					<div class=&image menbre&>")
    print("						<img src=&..\data\photos\membres\R-",tab[i][7],".jpg& alt=&",tab[i][0],"&>")
    print("					</div>")
    print("					<div class=&texte&>")
    print("						<br>")
    print("						<h4>",tab[i][0]," ",tab[i][1]," </h4>")
    print("						<h5>",tab[i][3],"</h5>")
    print("						<img src=&..\data\icons\esp.png& alt=&-------& class=&esperluette&>")
    print("						<p>",tab[i][4],"</p>")
    print("					</div>")
    print("				</div>")

def trombien(tab):
    print("				<div class=&carte&>")
    print("					<div class=&image photoMenbre&>")
    print("						<img src=&..\data\photos\membres\R-",tab[i][7],".jpg& alt=&",tab[i][0],"&>")
    print("					</div>")
    print("					<div class=&texte&>")
    print("						<br>")
    print("						<h4>",tab[i][0]," ",tab[i][1]," </h4>")
    print("						<h5>",tab[i][5],"</h5>")
    print("						<img src=&..\data\icons\esp.png& alt=&-------& class=&esperluette&>")
    print("						<p>",tab[i][6],"</p>")
    print("					</div>")
    print("				</div>")


tab=lecture_donne("trombi.csv")
for i in range(1,len(tab)):
    trombifr(tab);
