from flask import Flask, render_template, request, jsonify, send_file
import os
from pathlib import Path
import uuid
from werkzeug.utils import secure_filename 
from pfee_code_v2 import GestionnaireExcelIntelligent

app = Flask(__name__)


BASE_DIR = Path(__file__).resolve().parent
app.config['UPLOAD_FOLDER'] = BASE_DIR / 'uploads'
app.config['RESULT_FOLDER'] = BASE_DIR / 'resultats_analyse'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)


gestionnaire = GestionnaireExcelIntelligent()
print("⏳ Entraînement du modèle ML...")
gestionnaire.analyseur.entrainer_modele_intelligent()
print("✅ Modèle prêt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    
    print("👉 Requête reçue...")
    
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400

    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    
    file.save(filepath)

    try:
        print("⏳ Début de l'analyse...")
        
        df_result, result_path = gestionnaire.analyser_fichier_excel(
            filepath, 
            app.config['RESULT_FOLDER']
        )
        print(f"✅ Analyse terminée. {len(df_result)} lignes traitées.")

        if os.path.exists(filepath):
            os.remove(filepath)

        if df_result is None or df_result.empty:
            return jsonify({'error': 'Aucun avis valide trouvé ou fichier vide'}), 500

        
        total = len(df_result)
        sentiments = df_result['sentiment_final'].value_counts().to_dict()
        langues = df_result['langue'].value_counts().to_dict()
        confiance = round(float(df_result['confiance_final'].mean()) * 100, 1)
        
        preview = df_result[['avis', 'langue', 'sentiment_final', 'confiance_final']].head(5).to_dict(orient='records')

        return jsonify({
            "status": "success",
            "total": total,
            "distribution": sentiments,
            "langues": langues,
            "confiance": confiance,
            "preview": preview,
            "download_url": f"/download/{Path(result_path).name}"
        })

    except Exception as e:
        print(f"❌ ERREUR : {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': f"Erreur serveur: {str(e)}"}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(os.path.join(app.config['RESULT_FOLDER'], filename), as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'Fichier introuvable'}), 404

if __name__ == "__main__":
    app.run(debug=False, port=5000)
    