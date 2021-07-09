# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 08:29:24 2021

@author: Pablo Minué Estirado
"""

from numpy import random

def tonality ():
    tonalidad = input('Introduzca aqui la tonalidad (C, D, E, F...): ')
    print ('La tonalidad escogida es: ',tonalidad)
    return(tonalidad)

tonalidad = tonality()
ext=input('¿Desea acordes con extensiones? (maj7, m6, etc) y/n:')
if ext in ['yes','y','True','si','s']:
    ext = True
else:
    ext = False
notas=[1,2,3,4,5,6,7,8,9,10,11,12]
#major_scale=[1,3,5,6,8,10,12]
I=notas[0]
ii=notas[2]
bIII=notas[3]
iii=notas[4]
IV=notas[5]
V=notas[7]
bIV=notas[8]
vi=notas[9]
vii=notas[11]

estrofa1=[]
estrofa2=[]
estribillo=[]
puente=[]

#DEFINICION DE ACORDES FUNCIONALES

def dominant():
    probability = random.rand()
    if probability < 0.85:
        dominant = V
    else:
        dominant = vii
    
    return dominant

def subdominant():
    probability = random.rand()
    if probability < 0.6:
        subdominant = IV
    elif probability >= 0.6 and probability < 0.9:
        subdominant = ii
    elif probability >= 0.9 and probability < 0.95:
        subdominant = bIV
    else:
        subdominant = bIII
    
    return subdominant

def tonic():
    probability = random.rand()
    if probability < 0.7:
        tonic = I
    elif probability >= 0.7 and probability < 0.85:
        tonic = vi
    else:
        tonic = iii
    return tonic

def translation(lista,ext):
    notacion_sostenidos=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    notacion_bemoles=['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
    major_ext=['maj7','add9','add11','sus2','sus4']
    minor_ext=['7','6']
    if tonalidad in ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#']:
        for j in range (0,len(lista)):
            pos = notacion_sostenidos.index(tonalidad)
            nota = lista[j]-1+pos
            contador = pos
            for contador in range (pos, pos+12):
                if nota == contador:
                    if lista[j] in [3,5,10]:
                        if ext == True:
                            r = random.rand()
                            if r>0.7:
                                if r<0.85:
                                    lista[j]= notacion_sostenidos[nota]+'m'+minor_ext[0]
                                else:
                                    lista[j]= notacion_sostenidos[nota]+'m'+minor_ext[1]
                            else:
                                lista[j]= notacion_sostenidos[nota]+'m'
                        else:
                            lista[j]= notacion_sostenidos[nota]+'m'
                    elif lista[j] == 12:
                        if ext == True:
                            r = random.rand()
                            if r>0.7:  
                                lista[j]= notacion_sostenidos[nota]+'m7b5'
                            else:
                                lista[j]= notacion_sostenidos[nota]+'dim'
                        else:    
                            lista[j]= notacion_sostenidos[nota]+'dim'
                    else:
                        if ext == True:
                            r=random.rand()
                            p=0.7
                            if r>p:
                                z=0.3/5
                                for i in range (len(major_ext)):
                                    w=p+z
                                    if r>p and r<w:
                                        if lista[j] == 1:
                                            h=random.rand()
                                            if h>0.85:
                                                lista[j]=notacion_sostenidos[nota]+'maj7'
                                                p=p+z
                                            else:
                                                lista[j]=notacion_sostenidos[nota]
                                                p=p+z
                                        elif lista[j] == 8:
                                            lista[j]=notacion_sostenidos[nota]+'7'
                                            p=p+z
                                        else:
                                            extension=major_ext[i]
                                            lista[j]=notacion_sostenidos[nota]+extension
                                            p=p+z
                                    else:
                                        p=p+z
                            else:
                                lista[j]=notacion_sostenidos[nota]
                        else:
                            lista[j]=notacion_sostenidos[nota]
                else:
                    contador=contador + 1
            
    
    else:
        for j in range (0,len(lista)):
            pos = notacion_bemoles.index(tonalidad)
            nota = lista[j]-1+pos
            contador = pos
            for contador in range (pos, pos+12):
                if nota == contador:
                    if lista[j] in [3,5,10]:
                        if ext == True:
                            r = random.rand()
                            if r>0.7:
                                if r<0.85:
                                    lista[j]= notacion_bemoles[nota]+'m'+minor_ext[0]
                                else:
                                    lista[j]= notacion_bemoles[nota]+'m'+minor_ext[1]
                            else:
                                lista[j]= notacion_bemoles[nota]+'m'
                        else:
                            lista[j]= notacion_bemoles[nota]+'m'
                    elif lista[j] == 12:
                        if ext == True:
                            r = random.rand()
                            if r>0.7:  
                                lista[j]= notacion_bemoles[nota]+'m7b5'
                            else:
                                lista[j]= notacion_bemoles[nota]+'dim'
                        else:    
                            lista[j]= notacion_bemoles[nota]+'dim'
                    else:
                        if ext == True:
                            r=random.rand()
                            p=0.7
                            if r>p:
                                z=0.3/5
                                for i in range (len(major_ext)):
                                    w=p+z
                                    if r>p and r<w:
                                        if lista[j] == 1:
                                            h=random.rand()
                                            if h>0.85:
                                                lista[j]=notacion_bemoles[nota]+'maj7'
                                                p=p+z
                                            else:
                                                lista[j]=notacion_bemoles[nota]
                                                p=p+z
                                        elif lista[j] == 8:
                                            lista[j]=notacion_bemoles[nota]+'7'
                                            p=p+z
                                        else:
                                            extension=major_ext[i]
                                            lista[j]=notacion_bemoles[nota]+extension
                                            p=p+z
                                    else:
                                        p=p+z
                            else:
                                lista[j]=notacion_bemoles[nota]
                        else:
                            lista[j]=notacion_bemoles[nota]
                else:
                    contador=contador + 1
            
    
    return (lista)
        
# CREACION DE LA ESTROFA 1:
    
    #PRIMER ACORDE
def estrofa(estrofa1):
    probability = random.rand()
    if probability < 0.7:
        estrofa1.append(tonic())
        last_note='tonic'
    else:
        estrofa1.append(subdominant())
        last_note='subdominant'
        #SEGUNDO ACORDE
    if last_note == 'tonic':
        probability = random.rand()
        if probability < 0.8:
            estrofa1.append(subdominant())
            last_note='subdominant'
        elif probability >= 0.8 and probability <0.9:
            estrofa1.append(tonic())
            last_note='tonic'
        else:
            estrofa1.append(dominant())
            last_note='dominant'
    else:
        probability = random.rand()
        if probability < 0.5:
            estrofa1.append(dominant())
            last_note='dominant'
        elif probability >= 0.8 and probability <0.9:
            estrofa1.append(tonic())
            last_note='tonic'
        else:
            estrofa1.append(subdominant())
            last_note='subdominant'
    
    #TERCER ACORDE
    if last_note == 'tonic':
        probability = random.rand()
        if probability < 0.8:
            estrofa1.append(dominant())
            last_note='dominant'
        else:
            estrofa1.append(subdominant())
            last_note='subdominant'
    elif last_note == 'subdominant':
        probability = random.rand()
        if probability < 0.9:
            estrofa1.append(dominant())
            last_note='dominant'
        else:
            estrofa1.append(subdominant())
            last_note='subdominant'
            
    else:
        estrofa1.append(tonic())
        last_note='tonic'
    #CUARTO ACORDE (OPCIONAL)
    
    if last_note != 'tonic':
        estrofa1.append(tonic())
    return(estrofa1)
def printer(chords,section):
    print('\r\n',section,':','\r\n')
    printer=''
    for k in range (len(chords)):
        if k != len(chords)-1:
            printer = printer + chords[k] + ' - '
        else:
            printer = printer + chords[k]
    print(printer)
    print(printer)
    return(chords)    


estrofa1=estrofa(estrofa1)
estrofa1=translation(estrofa1,ext)

printer(estrofa1,'PRIMERA ESTROFA')

    
#### ESTRIBILLO

def estribillo(estribillo):
    estribillo=[]
    probability = random.rand()
    if probability < 0.7:
        estribillo.append(subdominant())
        last_note='subdominant'
    else:
        estribillo.append(tonic())
        last_note='tonic'
        #SEGUNDO ACORDE
    if last_note == 'tonic':
        probability = random.rand()
        if probability < 0.9:
            estribillo.append(subdominant())
            last_note='subdominant'
        else:
            estribillo.append(dominant())
            last_note='dominant'
    else:
        probability = random.rand()
        if probability < 0.9:
            estribillo.append(dominant())
            last_note='dominant'
        else:
            estribillo.append(subdominant())
            last_note='subdominant'
    
    #TERCER ACORDE
    if last_note == 'tonic':
        probability = random.rand()
        if probability < 0.8:
            estribillo.append(dominant())
            last_note='dominant'
        else:
            estribillo.append(subdominant())
            last_note='subdominant'
    elif last_note == 'subdominant':
        probability = random.rand()
        if probability < 0.9:
            estribillo.append(dominant())
            last_note='dominant'
        else:
            estribillo.append(subdominant())
            last_note='subdominant'
            
    else:
        estribillo.append(tonic())
        last_note='tonic'
    #CUARTO ACORDE (OPCIONAL)
    
    if last_note != 'tonic':
        y=random.rand()
        if y > 0.5:
            estribillo.append(1)
        else:
            estribillo.append(10)
    elif estribillo[2] == 5:
        estribillo.append(10)
    return(estribillo)

estribillo=estribillo(estribillo)
estribillo=translation(estribillo,ext)

printer(estribillo, 'ESTRIBILLO')

estrofa2=[]
estrofa2=translation(estrofa(estrofa2),ext)

printer(estrofa2, 'SEGUNDA ESTROFA')

printer(estribillo, 'ESTRIBILLO')
