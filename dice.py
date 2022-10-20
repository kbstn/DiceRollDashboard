#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:37:47 2022

@author: konrad
"""
import random
import streamlit as st
import pandas as pd

st.title('Werf mal!')

wuerfe = st.number_input('Anzahl der Wuerfe, immer wenn du die Zahl änderst wird neu gewürfelt! (nicht mehr als 500000 sonst ist das zuviel',value=20000)
if wuerfe > 500000:
    wuerfe = 500000
    
seiten = st.selectbox(
    'Wieviel Seiten hat dein "Würfel" 2 = Münze; 6= normaler Würfel; 20 = D20?',
    (2, 6, 20),index=1)

@st.cache(show_spinner=False)
def muenze(wuerfe,seiten):
    
    ergebnis= [0 for wurf in range(seiten)]
    label = [wurf+1 for wurf in range(seiten)]
    ergebnis_track =[]

    df=pd.DataFrame(columns=['run','results'])
    for i in range(wuerfe):
        wurf = random.randint(1,seiten)
        # print(wurf)
        
        ergebnis[wurf-1]+=1

        # wrong vektor in referencing the list??? i need to make a copy to fix it. apparently
        # [:]
        ergebnis_track.append(ergebnis[:])
    return ergebnis,ergebnis_track,label

ergebnis,ergebnis_track,label = muenze(wuerfe,seiten)

singel_ergebnis=pd.DataFrame(ergebnis).T
singel_ergebnis.columns=label
# st.write(singel_ergebnis)


df =pd.DataFrame(ergebnis_track,columns=label)

#

slider = st.slider('Wieviele der '+str(wuerfe)+' möchtest du dir anschauen?',1,wuerfe,value=6)

df2 = df[:slider]
# st.line_chart(df2)
st.write('Verteilung der ersten '+str(slider)+' Wuerfe')
st.bar_chart(df2)

st.write('Verteilung aller '+str(wuerfe)+' Wuerfe')

st.bar_chart(singel_ergebnis.T)
st.line_chart(df)