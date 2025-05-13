import streamlit as st
import pickle
import numpy as np

# Chargement du modèle entraîné
with open("C:/Users/HP/Desktop/ia/machine_learning.ipynb/classification.ipynb/model_RF.pkl", "rb") as f:
    model = pickle.load(f)

# Titre de l'application
st.title("🎓 Prédiction du résultat d'un étudiant (Pass / Fail)")

st.write("Entrez les notes de l'étudiant pour prédire s'il va réussir ou échouer.")

# Saisie des notes
hindi = st.slider("Note en Hindi", 0, 100, 50)
english = st.slider("Note en Anglais", 0, 100, 50)
science = st.slider("Note en Science", 0, 100, 50)
maths = st.slider("Note en Mathématiques", 0, 100, 50)
history = st.slider("Note en Histoire", 0, 100, 50)
geography = st.slider("Note en Géographie", 0, 100, 50)

# Calcul du total
total = hindi + english + science + maths + history + geography

# Bouton de prédiction
if st.button("Prédire"):
    input_data = np.array([[hindi, english, science, maths, history, geography, total]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ L'étudiant va **réussir (Pass)**.")
    else:
        st.error("❌ L'étudiant va **échouer (Fail)**.")
