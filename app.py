#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:37:47 2022

@author: konrad
"""
import random
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# add a title to the page
st.title('Werf mal!')

# create a input field which stores the given number in a variable
wuerfe = st.number_input('Anzahl der Wuerfe, immer wenn du die Zahl änderst wird neu gewürfelt! (nicht mehr als 100000 sonst ist das zuviel)',value=500)

# limit the app to 100k runs. otherwise it will crash my laptop
if wuerfe > 100000:
    wuerfe = 100000
    
# let the user select what to roll    
seiten = st.selectbox(
    'Wieviel Seiten hat dein "Würfel" 2 = Münze; 6= normaler Würfel; 20 = D20?',
    (2, 6, 20),index=1)

# Cache the following function to avoid recalculation everytime we query the resulting dataframe
@st.cache_data(show_spinner=False)
def muenze(wuerfe, seiten):
    """

    """
    
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

slider = st.slider('Wieviele der '+str(wuerfe)+' möchtest du dir anschauen?',1,wuerfe,value=12)

df2 = df[:slider]
# st.line_chart(df2)
st.write('Verteilung der ersten '+str(slider)+' Wuerfe')
st.bar_chart(df2)

st.write('Verteilung aller '+str(wuerfe)+' Wuerfe')

st.bar_chart(singel_ergebnis.T)
st.line_chart(df)