#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:00:42 2021

@author: joaquinvaras
"""
from numpy import random
cantidad=int(input("enter number of cards you want to play : "))
cartas=[]
i=1

while cantidad >= i:
    cartas.append(i)
    cartas.append(i)
    i+=1

i=0
mazo=[]
while len(mazo)!= cantidad*2:
    carta=cartas[random.randint(len(cartas))]
    mazo.append(carta)
    cartas.remove(carta)


n=0
while n * n <= cantidad*2:
    n+=1
    if n*n >= cantidad*2:
        break

i=0
linea=[]
tablero=[]
k=len(mazo)
while i<len(mazo):
    while len(linea)<n:
        if k>0:
            linea.append(mazo[i])
            i+=1
            k-=1
        else:
            linea.append(" ")
            i+=1
    tablero.append(linea)
    linea=[]
    

def game(columna):
    for e in columna:
        g = " "
        for t in e:
            g += "{:3}".format(str(t))
        print(g)

def twincards(cordx,cory,cordx2,cordy2,tablero):
    if tablero[cordy][cordx]==tablero[cordy2][cordx2]:
        return 1
    else:
        return 2

def void(cordx,cordy,cordx2,cordy2,tablero):
    tablero[cordy][cordx]="-"
    tablero[cordy2][cordx2]="-"
    return tablero

def turn(tablero,cord1,cord2,cordx2,cordy2,cantidad,tableroreal):
    fila1=[]
    fila=[]
    columna=[]
    i=0
    j=0
    cant=(cantidad*2)
    v=" "
    c=1
    f=0
    while len(fila1)<n+1:
        fila1.append(f)
        f+=1
    columna.append(fila1)
    
    while len(columna)<=n+1:
        while len(fila)<n+1:
            if cant <= 0:    
                fila.append(v)
            else:
                if len(fila)==0:
                    fila.append(str(len(columna)))

                if tableroreal[j][i]=="-":
                    fila.append("-")
                    i+=1
                elif (cord2==j+1 and cord1==i+1) or (cordx2==i+1 and cordy2==j+1):
                    fila.append(tablero[j][i])
                    i+=1
                

                elif columna[j][i]!=" ":    
                    fila.append("*")
                    i+=1
                else:
                    fila.append(" ")
                    i+=1

            cant-=1
        j+=1
        i=0
        columna.append(fila)
        fila=[]
    return columna

def turn1(tablero,cord1,cord2,cantidad,tableroreal):
    fila1=[]
    fila=[]
    columna=[]
    i=0
    j=0
    cant=(cantidad*2)
    v=" "
    c=1
    f=0
    while len(fila1)<n+1:
        fila1.append(f)
        f+=1
    columna.append(fila1)
    
    while len(columna)<=n+1:
        while len(fila)<n+1:
            if cant <= 0:    
                fila.append(v)
            else:
                if len(fila)==0:
                    fila.append(str(len(columna)))

                if tableroreal[j+1][i+1]=="-":
                    fila.append("-")
                    i+=1
                elif cord2==j+1 and cord1==i+1:
                    fila.append(tablero[j][i])
                    i+=1
                

                elif columna[j][i]!=" ":    
                    fila.append("*")
                    i+=1
                else:
                    fila.append(" ")
                    i+=1

            cant-=1
        j+=1
        i=0
        columna.append(fila)
        fila=[]
    return columna


p1=0
p2=0

fila1=[]
fila=[]
columna=[]
i=0
j=0
cant=(cantidad*2)
v=" "
c=1
f=0
while len(fila1)<n+1:
    fila1.append(f)
    f+=1
columna.append(fila1)
    
while len(columna)<=n+1:
    while len(fila)<n+1:
        if cant <= 0:    
            fila.append(v)
        else:
            if len(fila)==0:
                fila.append(str(len(columna)))
                

            if columna[j][i]!=" ":    
                fila.append("*")
                i+=1
            else:
                fila.append(" ")
                i+=1

        cant-=1
    j+=1
    i=0
    columna.append(fila)
    fila=[]
tableroreal=columna
print(game(columna))
    
while p1+p2<cantidad:
    if p1+p2==0:
        pass
    else:
        print(game(tableroreal))
    cordx=int(input("Player 1, enter x coordinates of the first card: "))
    cordy=int(input("Player 1, enter y coordinates of the first card: "))
    
    print(game(turn1(tablero,cordx,cordy,cantidad,tableroreal)))
    cordx2=int(input("Player 1, enter x coordinates of the second card: "))
    cordy2=int(input("Player 1, enter y coordinates of the second card: "))
    print(game(turn(tablero,cordx,cordy,cordx2,cordy2,cantidad,tableroreal)))
    
    if twincards(cordx,cordy,cordx2,cordy2,turn(tablero,cordx,cordy,cordx2,cordy2,cantidad,tableroreal))==1:
        p1+=1
        tableroreal=void(cordx,cordy,cordx2,cordy2,tableroreal)
        print("""
              
        THEY ARE THE SAME!!!  
        
        """+"PLAYER 1 - "+str(p1)+" Ptos"+"""
        
        """)
    else:
        print("""
              
        THEY ARE`NT THE SAME!!!
        
        """+"PLAYER 1 - "+str(p1)+" Ptos"+"""
        """+"PLAYER 2 - "+str(p2)+" Ptos"+"""
        
        """)
    
    if p1+p2==0:
        pass
    elif p1+p2==cantidad:
        break
    else:
        print(game(tableroreal))
    cordx=int(input("Player 2, enter x coordinates of the first card: "))
    cordy=int(input("Player 2, enter y coordinates of the first card: "))
    print(game(turn1(tablero,cordx,cordy,cantidad,tableroreal)))
    cordx2=int(input("Player 2, enter x coordinates of the second card: "))
    cordy2=int(input("Player 2, enter y coordinates of the second card: "))
    print(game(turn(tablero,cordx,cordy,cordx2,cordy2,cantidad,tableroreal)))
    if twincards(cordx,cordy,cordx2,cordy2,turn(tablero,cordx,cordy,cordx2,cordy2,cantidad,tableroreal))==1:
        p2+=1
        tableroreal=void(cordx,cordy,cordx2,cordy2,tableroreal)
        print("""
              
        THEY ARE THE SAME!!!  
        
        """+"PLAYER 2 - "+str(p2)+" Ptos"+"""
        
        """)
    else:
        print("""
              
        THEY ARE`NT THE SAME!!!
        
        """+"PLAYER 1 - "+str(p1)+" Ptos"+"""
        """+"PLAYER 2 - "+str(p2)+" Ptos"+"""
        
        """)  

if p1>p2:
    print("PLAYER 1 WIN!!!")
elif p1==p2:
    print("ITS A DRAW!!")
else:
    print("PLAYER 2 WIN!!!")