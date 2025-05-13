import streamlit as st
import pickle
import numpy as np

# Chargement du modèle entraîné
with open("student_exam_visualisation/model_RF.pkl", "rb") as f:
    model = pickle.load(f)

# Titre de l'application
st.title("Prédiction du résultat d'un étudiant (Pass / Fail)")

st.write("Entrez les notes de l'étudiant pour prédire s'il va réussir ou échouer.")

# Saisie des notes
hindi = st.number_input("Note en Hindi", 0, 90, 50)
english = st.number_input("Note en Anglais", 0, 90, 50)
science = st.number_input("Note en Science", 0, 90, 50)
maths = st.number_input("Note en Mathématiques", 0, 90, 50)
history = st.number_input("Note en Histoire", 0, 90, 50)
geography = st.number_input("Note en Géographie", 0, 90, 50)

# # Calcul du total
# total = hindi + english + science + maths + history + geography

# Bouton de prédiction
if st.button("Prédire"):
    input_data = np.array([[hindi, english, science, maths, history, geography]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("L'étudiant va **réussir (Pass)**.")
    else:
        st.error("L'étudiant va **échouer (Fail)**.")

# --- Interface de visualisation ---
st.header("Visualisation des Graphiques")

if st.button("Visualisation"):
    st.subheader(" Corrélation entre les matières")
    st.image("student_exam_visualisation/graph_corr.png", use_column_width=True)

    st.subheader(" Distribution des Matières")
    st.image("student_exam_visualisation/histogram.png", use_column_width=True)

    st.subheader(" Boxplot des Notes")
    st.image("student_exam_visualisation/boxplot.png", use_column_width=True)

    st.subheader(" Distribution_Total_Resultat")
    st.image("student_exam_visualisation/Distribution_Total_Resultat.png", use_column_width=True)

    st.subheader(" Moyennes des notes selon le résultat (Pass / Fail)")
    st.image("student_exam_visualisation/Moyennes des notes selon le résultat.png", use_column_width=True)