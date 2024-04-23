from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model copy.pkl')

@app.route('/')
def home():
    return render_template('pages-register.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        Mat = float(request.form['Mat'])
        Mi1 = float(request.form['Mi1'])
        Total_S1 = float(request.form['Total_S1'])
        Moyenne_S1 = float(request.form['Moyenne_S1'])
        Resultat_S1 = float(request.form['Résultat_S1'])
        Mi2 = float(request.form['Mi2'])
        Total_S2 = float(request.form['Total_S2'])
        Moyenne_S2 = float(request.form['Moyenne_S2'])
        Resultat_S2 = float(request.form['Résultat_S2'])

       # Vérifier si les champs ne sont pas vides
        if '' in [Mat, Mi1, Total_S1, Moyenne_S1, Resultat_S1, Mi2, Total_S2, Moyenne_S2, Resultat_S2]:
            return render_template('pages-register.html', error_message1=' le champ dois être remplis')

        # Convertir les valeurs en nombres flottants
        Mat = float(Mat)
        Mi1 = float(Mi1)
        Total_S1 = float(Total_S1)
        Moyenne_S1 = float(Moyenne_S1)
        Resultat_S1 = float(Resultat_S1)
        Mi2 = float(Mi2)
        Total_S2 = float(Total_S2)
        Moyenne_S2 = float(Moyenne_S2)
        Resultat_S2 = float(Resultat_S2)

        # Vérifier si les notes ne dépassent pas 20
        if any(n > 20 for n in [Mat, Mi1, Moyenne_S1, Mi2, Moyenne_S2]):
            return render_template('pages-register.html', error_message2='La note ne doit pas dépasser 20')
        
        # Vérifier si les totaux ne dépassent pas 600
        if any(n > 600 for n in [Total_S1, Total_S2]):
            return render_template('pages-register.html', error_message3='Le Total ne doit pas dépasser 600')
       
       # Concaténation des caractéristiques
        final_features = [[Mat, Mi1, Total_S1, Moyenne_S1, Resultat_S1, Mi2, Total_S2, Moyenne_S2, Resultat_S2]]
        
        # Prédiction de probabilité
        probabilites_predites = model.predict_proba(final_features)

        # Convertir les probabilités en pourcentages
        pourcentage_predit = (probabilites_predites[0][1] * 100).round(2)

        return render_template('pages-register.html', prediction_text='Votre chance de réussite: {}'.format(pourcentage_predit))

if __name__ == "__main__":
    app.run(debug=True)
