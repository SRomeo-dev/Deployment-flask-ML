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
        # Récupérer les données du formulaire
        Mat = request.form['Mat']
        Mi1 = request.form['Mi1']
        Total_S1 = request.form['Total_S1']
        Moyenne_S1 = request.form['Moyenne_S1']
        Resultat_S1 = request.form['Résultat_S1']
        Mi2 = request.form['Mi2']
        Total_S2 = request.form['Total_S2']
        Moyenne_S2 = request.form['Moyenne_S2']
        Resultat_S2 = request.form['Résultat_S2']

        # Vérifier si les champs ne sont pas vides
        error_messages = {}
        if Mat == '':
            error_messages['Mat'] = 'Le champ est requis'
        elif not 0 <= float(Mat) <= 20:
            error_messages['Mat'] = 'La note doit être comprise entre 0 et 20'
        
        if Mi1 == '':
            error_messages['Mi1'] = 'Le champ est requis'
        elif not 0 <= float(Mi1) <= 20:
            error_messages['Mi1'] = 'La note doit être comprise entre 0 et 20'
        
        if Total_S1 == '':
            error_messages['Total_S1'] = 'Le champ est requis'
        elif not 0 <= float(Total_S1) <= 600:
            error_messages['Total_S1'] = 'La note doit être comprise entre 0 et 600'
        
        if Moyenne_S1 == '':
            error_messages['Moyenne_S1'] = 'Le champ est requis'
        elif not 0 <= float(Moyenne_S1) <= 20:
            error_messages['Moyenne_S1'] = 'La note doit être comprise entre 0 et 20'
        
        if Resultat_S1 == '2':
            error_messages['Résultat_S1'] = 'Le champ est requis'
        else:
            Resultat_S1 = (Resultat_S1)

        if Mi2 == '':
            error_messages['Mi2'] = 'Le champ est requis'
        elif not 0 <= float(Mi2) <= 20:
            error_messages['Mi2'] = 'La note doit être comprise entre 0 et 20'
        
        if Total_S2 == '':
            error_messages['Total_S2'] = 'Le champ est requis'
        elif not 0 <= float(Total_S2) <= 600:
            error_messages['Total_S2'] = 'La note doit être comprise entre 0 et 600'
        
        if Moyenne_S2 == '':
            error_messages['Moyenne_S2'] = 'Le champ est requis'
        elif not 0 <= float(Moyenne_S2) <= 20:
            error_messages['Moyenne_S2'] = 'La note doit être comprise entre 0 et 20'

        if Resultat_S2 == '3':
            error_messages['Résultat_S2'] = 'Le champ est requis'
        else:
            Resultat_S2 = (Resultat_S2)


        if error_messages:
            return render_template('pages-register.html', error_messages=error_messages)

        # Convertir les valeurs en nombres flottants
        Mat = float(Mat)
        Mi1 = float(Mi1)
        Total_S1 = float(Total_S1)
        Moyenne_S1 = float(Moyenne_S1)
        Resultat_S1 = Resultat_S1
        Mi2 = float(Mi2)
        Total_S2 = float(Total_S2)
        Moyenne_S2 = float(Moyenne_S2)
        Resultat_S2 = Resultat_S2

        # Concaténation des caractéristiques
        final_features = [[Mat, Mi1, Total_S1, Moyenne_S1, Resultat_S1, Mi2, Total_S2, Moyenne_S2, Resultat_S2]]
        
        # Prédiction de probabilité
        probabilites_predites = model.predict_proba(final_features)

        # Convertir les probabilités en pourcentages
        pourcentage_predit = (probabilites_predites[0][1] * 100).round(2)

        return render_template('pages-register.html', prediction_text='Votre chance de réussite: {} %'.format(pourcentage_predit))
if __name__ == "__main__":
    app.run(debug=True)
