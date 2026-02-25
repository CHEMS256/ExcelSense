SentimentScan - Analyse Intelligente des Avis Clients
SentimentScan LogoVersionLicenseDocker

Analyse automatisée des sentiments et des langues pour les avis clients via un système hybride intelligent

🚀 Déployer • 📖 Documentation • 🐛 Issues • 💬 Support
📋 Table des Matières
À Propos
🌟 Fonctionnalités
🏗️ Architecture
🧠 Système Hybride Intelligent
🚀 Démarrage Rapide
📦 Installation
🎯 Utilisation
🚀 Déploiement
📚 Documentation
🤝 Contribuer
📄 Licence
📞 Support
🎯 À Propos
SentimentScan est une application web dockerisée conçue pour les administrateurs et analystes souhaitant traiter des volumes de retours clients. Elle combine la rapidité de l'analyse par mots-clés et la puissance du Machine Learning pour fournir une analyse de sentiment précise (Positif, Neutre, Négatif) et une détection de langue avancée (Français, Anglais, Arabe, Darija).

🎯 Objectif Principal
Optimiser le traitement des avis clients en automatisant l'analyse sentimentale sans recourir à des modèles Deep Learning lourds, permettant ainsi un déploiement sur des infrastructures légères et peu coûteuses.

🌟 Fonctionnalités
🧠 Analyse Intelligente Hybride
Double Moteur : Combinaison de l'analyse par mots-clés contextuels et d'un modèle ML (TF-IDF + RandomForest).
Sélection par Confiance : Le résultat final est choisi en fonction du score de confiance le plus élevé.
Entraînement Unique : Le modèle est entraîné au démarrage de l'application pour une réponse instantanée.
🌍 Détection Multilingue
Langues Supportées : Français, Anglais, Arabe, Darija Marocaine.
Nettoyage Automatique : Prétraitement du texte (minuscule, suppression du bruit) et gestion des caractères arabes.
📊 Rapports et Statistiques
Tableau de Bord : Distribution des sentiments, répartition des langues, score de confiance moyen.
Export Excel : Fichier résultat détaillé (Avis original, Langue, Sentiment, Confiance, N° de ligne).
Prévisualisation : Affichage des 5 premiers avis analysés en temps réel.
🔒 Sécurité et Performance
Légereté : Pas de base de données lourde, fichiers temporaires supprimés après traitement.
Sécurité : Validation stricte des types de fichiers, nommage sécurisé (UUID), limite de 16MB.
Interface Responsive : Design moderne adapté aux mobiles et tablettes.
🏗️ Architecture
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Frontend │ │ Backend │ │ Storage │
│ (Nginx) │◄──►│ (Flask) │◄──►│ (Temp FS) │
│ HTML/Tailwind │ │ Python 3.9 │ │ /tmp/uploads │
└─────────────────┘ └─────────────────┘ └─────────────────┘
│
▼
┌─────────────────┐
│ AI Engine │
│ ┌───────────┐ │
│ │ Keywords │ │
│ │ Analysis │ │
│ └───────────┘ │
│ ┌───────────┐ │
│ │ ML Model │ │
│ │(Sklearn) │ │
│ └───────────┘ │
└─────────────────┘

text


---

## 🧠 Système Hybride Intelligent

Le système utilise une approche en parallèle pour maximiser la précision :

1.  **Analyseur Lexical** : Scan rapide basé sur des dictionnaires de sentiments prédéfinis.
2.  **Analyseur ML** : Vectorisation TF-IDF et classification via RandomForest.
3.  **Décision Finale** : Comparaison des scores de confiance. Le système sélectionne la prédiction la plus sûre.

---

## 🚀 Démarrage Rapide

### Prérequis

- [Docker](https://www.docker.com/) (version 20.10+)
- [Docker Compose](https://docs.docker.com/compose/) (version 1.29+)
- [Git](https://git-scm.com/)

### Installation en 3 Commandes

```bash
# 1. Cloner le projet
git clone https://github.com/yourusername/sentimentscan.git
cd sentimentscan

# 2. Configurer l'environnement
cp .env.example .env

# 3. Lancer l'application
docker-compose up -d
Accès à l'Application
Ouvrez votre navigateur et accédez à :

Application : http://localhost:5000
Téléchargement : Interface Web prête à l'emploi
📦 Installation Détaillée
1. Clonage du Projet
bash

git clone https://github.com/yourusername/sentimentscan.git
cd sentimentscan
2. Configuration de l'Environnement
bash

# Copier le fichier d'environnement
cp .env.example .env

# Éditer avec vos informations
nano .env
Variables à configurer :

env

# Application
FLASK_ENV=production
SECRET_KEY=votre_clé_secrète_très_longue
UPLOAD_FOLDER=/tmp/uploads
MAX_CONTENT_LENGTH=16777216  # 16MB Limit

# Sécurité
ALLOWED_EXTENSIONS=xlsx,xls,csv
3. Lancement
bash

# Construction et lancement
docker-compose up -d --build

# Vérification des services
docker-compose ps
🎯 Utilisation
Importation de Fichiers
Accéder à l'interface : Ouvrez l'URL de l'application.
Télécharger : Glissez-déposez ou sélectionnez votre fichier Excel/CSV.
Détection Auto : Le système détecte automatiquement la colonne contenant les avis (ex: "avis", "commentaire").
Analyser : Cliquez sur le bouton "Analyser".
Consultation des Résultats
Statistiques : Visualisez le nombre total, la distribution des sentiments et des langues.
Détails : Consultez la prévisualisation des 5 premiers avis.
Export : Cliquez sur "Télécharger les résultats" pour obtenir le fichier Excel analysé.
🚀 Déploiement
Railway (Recommandé)
<div align="center">

Deploy on Railway

</div>

bash

# Installation CLI
npm install -g railway

# Déploiement
railway login
railway init
railway up
Render
<div align="center">

Deploy to Render

</div>

Créez un compte sur Render.
Connectez votre dépôt GitHub.
Sélectionnez "Web Service" et laissez Render détecter le Dockerfile.
Heroku
bash

npm install -g heroku
heroku login
heroku create sentimentscan
heroku container:login
heroku container:push web -a sentimentscan
heroku container:release web -a sentimentscan
📚 Documentation
Processus de Traitement
Étape
Description
Upload	Validation du type et de la taille du fichier.
Parsing	Lecture Excel/CSV et détection automatique de la colonne cible.
Nettoyage	Mise en minuscule, suppression du bruit, gestion des caractères arabes.
Analyse	Exécution parallèle du moteur lexical et du modèle ML.
Résultat	Génération du fichier Excel et mise à jour des statistiques.
Nettoyage	Suppression automatique du fichier original uploadé.

Structure du Fichier de Sortie
Le fichier Excel téléchargé contient les colonnes suivantes :

Avis Original : Le texte complet de l'avis.
Langue Détectée : FR, EN, AR, Darija.
Sentiment : Positif, Neutre, Négatif.
Score de Confiance : Pourcentage de certitude (0% à 100%).
N° Ligne Original : Référence pour retrouver l'avis dans le fichier source.
🤝 Contribuer
Nous apprécions vos contributions !

🐛 Rapporter des Bugs
Utilisez les issues GitHub.
Incluez le fichier problématique (anonymisé) si possible.
💡 Suggérer des Améliorations
Idées pour améliorer la détection de la Darija.
Optimisation du modèle ML pour les CPU basiques.
🔧 Étapes
Fork le projet
Créez une branche (git checkout -b feature/darija-improvement)
Commitez vos changements (git commit -m 'Improve Darija detection')
Pushez (git push origin feature/darija-improvement)
Ouvrez une Pull Request
📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

text

MIT License

Copyright (c) 2024 SentimentScan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

⚠️ Limitations Connues
La détection de la Darija est expérimentale et repose sur des heuristiques.
La taille des fichiers est limitée à 16MB pour garantir la stabilité sur les petits serveurs.
🌟 Remerciements
Merci aux contributeurs des bibliothèques open-source utilisées : Scikit-learn, Pandas, Flask.

<div align="center">

⭐ Si ce projet vous a aidé, n'oubliez pas de laisser une étoile !


🔝 Retour en haut

</div>
