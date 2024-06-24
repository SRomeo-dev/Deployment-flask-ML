from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('pages-register.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        form_data = {
            'Mat': request.form.get('Mat'),
            'Mi1': request.form.get('Mi1'),
            'Total_S1': request.form.get('Total_S1'),
            'Moyenne_S1': request.form.get('Moyenne_S1'),
            'Résultat_S1': request.form.get('Résultat_S1'),
            'Mi2': request.form.get('Mi2'),
            'Total_S2': request.form.get('Total_S2'),
            'Moyenne_S2': request.form.get('Moyenne_S2'),
            'Résultat_S2': request.form.get('Résultat_S2')
        }

        valid_values = {}
        error_messages = {}

        # Fonction de validation pour les champs
        def validate_field(field, value, min_val, max_val, error_msg):
            if value == '':
                error_messages[field] = 'Le champ est requis'
            elif not min_val <= float(value) <= max_val:
                error_messages[field] = error_msg
            else:
                valid_values[field] = value

        # Validation des champs
        validate_field('Mat', form_data['Mat'], 0, 20, 'La note doit être comprise entre 0 et 20')
        validate_field('Mi1', form_data['Mi1'], 0, 20, 'La note doit être comprise entre 0 et 20')
        validate_field('Total_S1', form_data['Total_S1'], 0, 600, 'Le total doit être compris entre 0 et 600')
        validate_field('Moyenne_S1', form_data['Moyenne_S1'], 0, 20, 'La moyenne doit être comprise entre 0 et 20')
        validate_field('Mi2', form_data['Mi2'], 0, 20, 'La note doit être comprise entre 0 et 20')
        validate_field('Total_S2', form_data['Total_S2'], 0, 600, 'Le total doit être compris entre 0 et 600')
        validate_field('Moyenne_S2', form_data['Moyenne_S2'], 0, 20, 'La moyenne doit être comprise entre 0 et 20')

        # Validation des résultats
        if form_data['Résultat_S1'] == '2':
            error_messages['Résultat_S1'] = 'Le champ est requis'
        else:
            valid_values['Résultat_S1'] = form_data['Résultat_S1']

        if form_data['Résultat_S2'] == '3':
            error_messages['Résultat_S2'] = 'Le champ est requis'
        else:
            valid_values['Résultat_S2'] = form_data['Résultat_S2']

        if error_messages:
            return render_template('pages-register.html', error_messages=error_messages, valid_values=valid_values)

        # Conversion des valeurs en nombres flottants
        final_features = [
            [
                float(form_data['Total_S1']),
                float(form_data['Moyenne_S1']),
                form_data['Résultat_S1'],
                float(form_data['Total_S2']),
                float(form_data['Moyenne_S2']),
                form_data['Résultat_S2'],
                float(form_data['Mat']),
                float(form_data['Mi1']),
                float(form_data['Mi2'])
            ]
        ]

        # Prédiction de probabilité
        probabilites_predites = model.predict_proba(final_features)
        pourcentage_predit = (probabilites_predites[0][1] * 100).round(2)
        prediction_available = True

        # Classe CSS pour le texte
        text_color_class = 'text-success' if pourcentage_predit >= 50 else 'text-danger'

        return render_template(
            'pages-register.html',
            prediction_text=f'Votre chance de réussite est de: {pourcentage_predit} %',
            prediction_available=prediction_available,
            text_color_class=text_color_class
        )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

# Pour tléphone: 192.168.137.1:5000