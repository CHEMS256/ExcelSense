
ExcelSense - Analyse de Sentiments Intelligente
VersionLicensePython
Automatisation de l'analyse de sentiments pour les avis clients via le Machine Learning et le traitement du langage naturel (NLP).

🚀 Déployer • 📖 Documentation • 🐛 Issues • 💬 Support
📋 Table des Matières
À Propos
🌟 Fonctionnalités
🏗️ Architecture
🚀 Démarrage Rapide
📦 Installation Détaillée
🎯 Utilisation
🚀 Déploiement
📚 Documentation
🤝 Contribuer
📄 Licence

ExcelSense est une application web intelligente conçue pour analyser les fichiers Excel contenant des avis clients. Elle utilise une approche hybride combinant un classificateur Machine Learning (Random Forest) et une analyse contextuelle basée sur des dictionnaires pour fournir des résultats précis, même pour des langues mixtes comme le Darija (Marocain).

🎯 Objectif Principal
Transformer des fichiers bruts d'avis clients en tableaux de bord statistiques clés, en identifiant automatiquement la langue, le sentiment (Positif, Négatif, Neutre) et le niveau de confiance.

🌟 Fonctionnalités
🧠 Analyse Hybride
Machine Learning : Classificateur RandomForest avec vectorisation TF-IDF.
Analyse Contextuelle : Dictionnaires prédéfinis pour les expressions idiomatiques.
Fusion Intelligente : Sélection automatique de la meilleure analyse basée sur le score de confiance.
🌐 Multilinguisme
Détection Automatique : Français, Anglais, Arabe littéraire.
Support Darija : Reconnaissance spécifique des expressions marocaines (ex: "زوين", "خايب", "مزيان").
📊 Rapports et Données
Import Flexible : Support des formats .xlsx, .xls et .csv.
Statistiques Instantanées : Distribution des sentiments, répartition par langue, confiance moyenne.
Export Excel : Téléchargement du fichier analysé avec métadonnées complètes.
🏗️ Architecture
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐│   Frontend      │    │    Backend      │    │    Fichiers     ││   (HTML/JS)     │◄──►│   (Flask)       │◄──►│   (Excel/CSV)   ││   Bootstrap     │    │   Python 3.9    │    │   Uploads       │└─────────────────┘    └─────────────────┘    └─────────────────┘                              │                              ▼                       ┌─────────────────┐                       │   Moteur NLP    │                       │  ┌───────────┐  │                       │  │   ML      │  │                       │  │(Sklearn)  │  │                       │  └───────────┘  │                       │  ┌───────────┐  │                       │  │ LangDetect│  │                       │  └───────────┘  │                       └─────────────────┘
🚀 Démarrage Rapide
Prérequis
Python 3.9+
pip (Gestionnaire de paquets Python)
Git
Installation en 3 Commandes
bash

# 1. Cloner le projet
git clone https://github.com/yourusername/pfee-sentiment.git
cd ExcelSense
# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python app.py
Accès à l'Application
Ouvrez votre navigateur et accédez à :

Application : http://localhost:5000
Upload : http://localhost:5000/upload (POST)
📦 Installation Détaillée
1. Clonage du Projet
bash

git clone https://github.com/yourusername/pfee-sentiment.git
cd ExcelSense
2. Environnement Virtuel (Recommandé)
bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Installation des Dépendances
bash

pip install flask pandas numpy scikit-learn langdetect openpyxl werkzeug
(Ou utilisez requirements.txt si fourni)

4. Structure des Dossiers
Assurez-vous que les dossiers suivants existent (l'application tente de les créer automatiquement) :

uploads/ : Stockage temporaire des fichiers entrants.
resultats_analyse/ : Stockage des fichiers Excel analysés.
🎯 Utilisation
Via l'Interface Web (Frontend)
Accédez à la page d'accueil (/).
Sélectionnez un fichier Excel ou CSV contenant une colonne d'avis.
Cliquez sur "Analyser".
Consultez les statistiques (graphiques, prévisualisation) et téléchargez le rapport.
Via l'API (Backend)
Envoyer un fichier à analyser
bash

curl -X POST http://localhost:5000/upload \
  -F 'file=@chemin/vers/votre_fichier.xlsx'
Réponse JSON attendue
json

{
  "status": "success",
  "total": 150,
  "distribution": {"positif": 80, "negatif": 40, "neutre": 30},
  "langues": {"fr": 100, "darija": 30, "en": 20},
  "confiance": 85.4,
  "download_url": "/download/analyse_20240521_143000.xlsx"
}
Télécharger le résultat
Accédez à l'URL retournée dans download_url via le navigateur ou curl.

🚀 Déploiement
Docker (Recommandé pour la production)
Créez un Dockerfile :

dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
Build et Run :

bash

docker build -t ExcelSense .
docker run -p 5000:5000 ExcelSense
Heroku
bash

heroku create ExcelSense
git push heroku main
Railway / Render
Connectez votre dépôt GitHub et définissez la commande de démarrage : python app.py.
Note : Assurez-vous de configurer un volume persistant pour le dossier resultats_analyse si vous souhaitez conserver l'historique.

📚 Documentation
Endpoints API
Méthode
Endpoint
Description
GET	/	Page d'accueil (Interface Upload)
POST	/upload	Télécharger et analyser un fichier
GET	/download/<filename>	Télécharger le fichier analysé

Logique de Détection (pfee_code_v2.py)
Pré-traitement : Nettoyage du texte, mise en minuscule.
Détection Langue : Priorité aux caractères Arabes/Darija, puis langdetect pour Fr/En.
Scoring :
Contextuel : Recherche de mots-clés positifs/négatifs connus.
ML : Prédiction via le modèle entraîné.
Fusion : Comparaison des scores de confiance pour choisir le résultat final.
🤝 Contribuer
Nous apprécions vos contributions pour améliorer la détection du Darija ou optimiser le modèle ML.

🔧 Étapes
Fork le projet.
Créez une branche (git checkout -b feature/amelioration-darija).
Commitez vos changements (git commit -m 'Ajout lexique Darija').
Pushez (git push origin feature/amelioration-darija).
Ouvrez une Pull Request.
📄 Licence
Ce projet est sous licence MIT.

MIT License

Copyright (c) 2024 PfeeSentiment

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
