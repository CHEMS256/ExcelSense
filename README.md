```markdown
# ExcelSense - Analyse de Sentiments Intelligente

<div align="center">
  <img src="https://img.shields.io/badge/Version-2.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.9+-9cf.svg" alt="Python">
</div>

> Automatisation de l'analyse de sentiments pour les avis clients via le Machine Learning et le traitement du langage naturel (NLP).

<div align="center">
  <a href="#-démarrage-rapide">🚀 Déployer</a> •
  <a href="#-documentation">📖 Documentation</a> •
  <a href="#-contribuer">🐛 Issues</a> •
  <a href="#-support">💬 Support</a>
</div>

## 📋 Table des Matières
- [À Propos](#-à-propos)
- [🌟 Fonctionnalités](#-fonctionnalités)
- [🏗️ Architecture](#️-architecture)
- [🚀 Démarrage Rapide](#-démarrage-rapide)
- [📦 Installation Détaillée](#-installation-détaillée)
- [🎯 Utilisation](#-utilisation)
- [🚀 Déploiement](#-déploiement)
- [📚 Documentation](#-documentation)
- [🤝 Contribuer](#-contribuer)
- [📄 Licence](#-licence)

## 🎯 À Propos

**ExcelSense** est une application web intelligente conçue pour analyser les fichiers Excel contenant des avis clients. Elle utilise une approche hybride combinant un classificateur Machine Learning (Random Forest) et une analyse contextuelle basée sur des dictionnaires pour fournir des résultats précis, même pour des langues mixtes comme le Darija (Marocain).

### 🎯 Objectif Principal
Transformer des fichiers bruts d'avis clients en tableaux de bord statistiques clés, en identifiant automatiquement la langue, le sentiment (Positif, Négatif, Neutre) et le niveau de confiance.

## 🌟 Fonctionnalités

### 🧠 Analyse Hybride
- **Machine Learning** : Classificateur RandomForest avec vectorisation TF-IDF (caractères N-grams).
- **Analyse Contextuelle** : Dictionnaires prédéfinis pour les expressions idiomatiques.
- **Fusion Intelligente** : Sélection automatique de la meilleure analyse basée sur le score de confiance.

### 🌐 Multilinguisme
- **Détection Automatique** : Français, Anglais, Arabe littéraire.
- **Support Darija** : Reconnaissance spécifique des expressions marocaines (ex: "زوين", "خايب", "مزيان").

### 📊 Rapports et Données
- **Import Flexible** : Support des formats `.xlsx`, `.xls` et `.csv`.
- **Statistiques Instantanées** : Distribution des sentiments, répartition par langue, confiance moyenne.
- **Export Excel** : Téléchargement du fichier analysé avec métadonnées complètes.

## 🏗️ Architecture

```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │    Fichiers     │
│   (HTML/JS)     │◄──►│   (Flask)       │◄──►│   (Excel/CSV)   │
│   Bootstrap     │    │   Python 3.9    │    │   Uploads       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Moteur NLP    │
                       │  ┌───────────┐  │
                       │  │   ML      │  │
                       │  │(Sklearn)  │  │
                       │  └───────────┘  │
                       │  ┌───────────┐  │
                       │  │ LangDetect│  │
                       │  └───────────┘  │
                       └─────────────────┘
```

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.9+
- pip (Gestionnaire de paquets Python)
- Git

### Installation en 3 Commandes

```bash
# 1. Cloner le projet
git clone https://github.com/yourusername/excelsense.git
cd excelsense

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python app.py
```

### Accès à l'Application
Ouvrez votre navigateur et accédez à :
- **Application** : http://localhost:5000
- **API Endpoint** : http://localhost:5000/upload

## 📦 Installation Détaillée

### 1. Clonage du Projet
```bash
git clone https://github.com/yourusername/excelsense.git
cd excelsense
```

### 2. Environnement Virtuel (Recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Installation des Dépendances
Créez un fichier `requirements.txt` contenant :
```text
flask
pandas
numpy
scikit-learn
langdetect
openpyxl
werkzeug
```
Puis installez :
```bash
pip install -r requirements.txt
```

### 4. Structure des Dossiers
L'application créera automatiquement les dossiers nécessaires au démarrage :
- `uploads/` : Stockage temporaire des fichiers entrants.
- `resultats_analyse/` : Stockage des fichiers Excel analysés.

## 🎯 Utilisation

### Via l'Interface Web
1. Accédez à la page d'accueil (`/`).
2. Sélectionnez un fichier Excel ou CSV contenant une colonne d'avis (ex: "avis", "comment", "text").
3. Cliquez sur "Analyser".
4. Consultez les statistiques instantanées (graphiques, prévisualisation).
5. Téléchargez le rapport Excel complet.

### Via l'API (cURL)

#### Envoyer un fichier à analyser
```bash
curl -X POST http://localhost:5000/upload \
  -F 'file=@chemin/vers/votre_fichier.xlsx'
```

#### Réponse JSON attendue
```json
{
  "status": "success",
  "total": 150,
  "distribution": {"positif": 80, "negatif": 40, "neutre": 30},
  "langues": {"fr": 100, "darija": 30, "en": 20},
  "confiance": 85.4,
  "download_url": "/download/analyse_20240521_143000.xlsx"
}
```

## 🚀 Déploiement

### Docker (Recommandé)

Créez un `Dockerfile` à la racine :
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build et Run :
```bash
docker build -t excelsense-app .
docker run -p 5000:5000 excelsense-app
```

### Heroku / Railway
1. Connectez votre dépôt GitHub.
2. Définissez la commande de démarrage : `python app.py`.
3. Assurez-vous que `Python` est détecté comme environnement.

## 📚 Documentation

### Endpoints API

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Page d'accueil (Interface Upload) |
| POST | `/upload` | Télécharger et analyser un fichier |
| GET | `/download/<filename>` | Télécharger le fichier analysé |

### Logique de Détection (pfee_code_v2.py)
Le moteur d'analyse suit ce processus :
1. **Pré-traitement** : Nettoyage du texte, mise en minuscule.
2. **Détection Langue** : Priorité aux caractères Arabes/Darija, puis `langdetect` pour Fr/En.
3. **Double Analyse** :
   - *Contextuelle* : Recherche de mots-clés connus (Darija inclus).
   - *ML* : Prédiction via RandomForest entraîné sur les données synthétiques.
4. **Fusion** : Comparaison des scores de confiance pour choisir le résultat final le plus fiable.

## 🤝 Contribuer

Les contributions sont les bienvenues pour enrichir les dictionnaires (surtout Darija) ou améliorer le modèle ML.

1. Fork le projet.
2. Créez une branche (`git checkout -b feature/nouvelle-fonction`).
3. Commitez (`git commit -m 'Ajout fonction'`).
4. Pushez (`git push origin feature/nouvelle-fonction`).
5. Ouvrez une Pull Request.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

MIT License

Copyright (c) 2024 ExcelSense

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

