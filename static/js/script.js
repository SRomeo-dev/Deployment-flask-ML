// JavaScript pour désactiver la sélection de l'option "Choisissez une valeur"
function disablePlaceholderOption1() {
  var select = document.getElementById("selectValue");
  var placeholderOption = select.options[0];
  placeholderOption.disabled = true;
}

// JavaScript pour désactiver la sélection de l'option "Choisissez une valeur"
function disablePlaceholderOption2() {
  var select = document.getElementById("selectValue2");
  var placeholderOption = select.options[0];
  placeholderOption.disabled = true;
}
// Fonction pour mettre à jour les moyennes et les résultats en fonction des totaux
function updateForm() {
  var totalS1 = parseFloat(document.getElementById("Total_S1").value);
  var totalS2 = parseFloat(document.getElementById("Total_S2").value);

  if (!isNaN(totalS1)) {
    var moyenneS1 = totalS1 / 30;
    document.getElementById("Moyenne_S1").value = moyenneS1.toFixed(2); // Arrondi à deux décimales
    // Sélectionne automatiquement le résultat en fonction de la moyenne
    if (moyenneS1 >= 10) {
      document.getElementById("selectValue").value = "1"; // Admis (e)
    } else {
      document.getElementById("selectValue").value = "0"; // Ajourné (e)
    }
  }

  if (!isNaN(totalS2)) {
    var moyenneS2 = totalS2 / 30;
    document.getElementById("Moyenne_S2").value = moyenneS2.toFixed(2); // Arrondi à deux décimales
    // Sélectionne automatiquement le résultat en fonction de la moyenne
    if (moyenneS2 >= 10) {
      document.getElementById("selectValue2").value = "1"; // Admis (e)
    } else {
      document.getElementById("selectValue2").value = "0"; // Ajourné (e)
    }
  }
}

// Écoute les événements de saisie dans les champs Total_S1 et Total_S2
document.getElementById("Total_S1").addEventListener("input", updateForm);
document.getElementById("Total_S2").addEventListener("input", updateForm);

// Appel initial pour mettre à jour les moyennes et les résultats si des valeurs sont déjà présentes au chargement de la page
updateForm();

document.addEventListener("DOMContentLoaded", function () {
  var acceptTermsCheckbox = document.getElementById("acceptTerms");
  var submitButton = document.querySelector("button[type='submit']");

  acceptTermsCheckbox.addEventListener("change", function () {
    submitButton.disabled = !acceptTermsCheckbox.checked;
  });

  // Désactiver initialement le bouton de soumission
  submitButton.disabled = true;
});
