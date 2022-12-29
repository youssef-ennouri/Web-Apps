import streamlit as st
import string 
from random import *

st.markdown("<h1 style='text-align: center; color: white;'>Password Generator</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>This Is A Web App To Allow Password Generation</h6>", unsafe_allow_html=True)

Majuscule = string.ascii_uppercase
Minuscule = string.ascii_lowercase
Digits = string.digits
Punctuation = string.punctuation
liste1 = []
liste2 = []

col1, col2, col3, col4 = st.columns(4)

with col1:
   majuscule = st.checkbox("Majuscule", value=True,label_visibility="visible")

with col2:
   minuscule = st.checkbox("Minuscule", value=True,label_visibility="visible")

with col3:
   chiffre = st.checkbox("Chiffre", value=True,label_visibility="visible")

with col4:
	symbole = st.checkbox("Symbole", value=True,label_visibility="visible")

longueur = st.slider("Longueur Du Mot De Passe", 0, 30, 15)

def generate():
	for x in range(int(longueur)):
		if majuscule :
			tirage1 = choice(Majuscule)
			liste1.append(tirage1)
		if minuscule :
			tirage2 = choice(Minuscule)
			liste1.append(tirage2)
		if chiffre :
			tirage3 = choice(Digits)
			liste1.append(tirage3)
		if symbole :
			tirage4 = choice(Punctuation)
			liste1.append(tirage4)
		D = choice(liste1)
		liste2.append(D)

	Mot_De_Passe = "".join(liste2)
	return Mot_De_Passe

container = st.container()
x = container.subheader(generate())
bouton = container.button("Generate", on_click=None, disabled=False)
