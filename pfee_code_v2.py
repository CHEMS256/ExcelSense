import pandas as pd
import numpy as np
import re
import warnings
from datetime import datetime
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from langdetect import detect, LangDetectException

warnings.filterwarnings("ignore")


class APIIntelligente:
    def detecter_langue(self, texte):
        if not texte or pd.isna(texte):
            return "fr"
        texte = str(texte).lower()

        
        if re.search(r'[\u0600-\u06FF]', texte):
            if any(w in texte for w in ['زوين', 'مزيان', 'خايب', 'ماعجبني', 'مربوط']):
                return 'darija'
            return 'ar'

        try:
            lang = detect(texte)
            return lang if lang in ['fr', 'en'] else 'fr'
        except LangDetectException:
            return 'fr'

    def analyser_expression_contextuelle(self, texte, langue):
        if not texte:
            return {'sentiment': 'neutre', 'confiance': 0}

        positif = {
            'fr': ['bon', 'excellent', 'super', 'génial', 'parfait', 'top', 'efficace'],
            'en': ['good', 'great', 'excellent', 'perfect', 'amazing', 'love'],
            'ar': ['ممتاز', 'جيد', 'رائع'],
            'darija': ['زوين', 'مزيان', 'مربوط', 'عجبني']
        }

        negatif = {
            'fr': ['mauvais', 'nul', 'horrible', 'déçu', 'lent', 'bug'],
            'en': ['bad', 'terrible', 'worst', 'slow', 'fail'],
            'ar': ['سيء', 'خايب', 'فاشل'],
            'darija': ['خايب', 'ماعجبني', 'ماشي مزيان', 'طايح']
        }

        score = 0
        
        
        for w in positif.get(langue, []):
            if w in texte:
                score += 1
        for w in negatif.get(langue, []):
            if w in texte:
                score -= 1

        if score > 0:
            return {'sentiment': 'positif', 'confiance': 0.8}
        if score < 0:
            return {'sentiment': 'negatif', 'confiance': 0.8}
        return {'sentiment': 'neutre', 'confiance': 0.4}


class AnalyseurSentimentsIntelligent:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=3000, analyzer='char_wb', ngram_range=(1,3))
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.api = APIIntelligente()
        self.is_trained = False

    def preprocess(self, s):
        return s.fillna("").astype(str).str.lower()

    def entrainer_modele_intelligent(self):
        
        data = {
            "avis": [
                "excellent produit", "très mauvais", "correct", "super service", "nul", 
                "je recommande", "désastre", "passable", "génial", "horrible", 
                "bon rapport qualité prix", "ne marche pas", "top", "déçu"
            ],
            "sentiment": [
                "positif", "negatif", "neutre", "positif", "negatif", 
                "positif", "negatif", "neutre", "positif", "negatif",
                "positif", "negatif", "positif", "negatif"
            ]
        }
        df = pd.DataFrame(data)
        X = self.vectorizer.fit_transform(df['avis'])
        self.model.fit(X, df['sentiment'])
        self.is_trained = True

    def analyser_batch(self, df, col):
        df = df.copy()
        df['texte'] = self.preprocess(df[col])
        
        
        df = df[df['texte'].str.len() > 2].reset_index(drop=True)
        
        if df.empty:
            return pd.DataFrame()

        df['langue'] = df['texte'].apply(self.api.detecter_langue)
        
        # Analyse Contextuelle
        ctx = df.apply(lambda r: self.api.analyser_expression_contextuelle(r[col], r['langue']), axis=1)
        df['ctx_sentiment'] = ctx.apply(lambda x: x['sentiment'])
        df['ctx_confiance'] = ctx.apply(lambda x: x['confiance'])

        # Analyse ML
        X = self.vectorizer.transform(df['texte'])
        df['ml_sentiment'] = self.model.predict(X)
        df['ml_confiance'] = self.model.predict_proba(X).max(axis=1)

        # Fusion
        df['sentiment_final'] = np.where(
            df['ctx_confiance'] > df['ml_confiance'],
            df['ctx_sentiment'],
            df['ml_sentiment']
        )

        df['confiance_final'] = np.maximum(df['ctx_confiance'], df['ml_confiance'])
        df['ligne_excel'] = df.index + 2

        return df.rename(columns={col: 'avis'})[
            ['ligne_excel', 'avis', 'langue', 'sentiment_final', 'confiance_final']
        ]


class GestionnaireExcelIntelligent:
    def __init__(self):
        self.analyseur = AnalyseurSentimentsIntelligent()

    def detecter_colonne_avis(self, df):
        for c in df.columns:
            c_lower = str(c).lower()
            if 'avis' in c_lower or 'comment' in c_lower or 'text' in c_lower or 'review' in c_lower:
                return c
        for c in df.columns:
            if df[c].dtype == 'object':
                return c
        return df.columns[0]

    
    def analyser_fichier_excel(self, path, output_dir):
        
        output_dir = Path(output_dir) 
        try:
            if path.endswith('.xlsx') or path.endswith('.xls'):
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
            
            if df.empty:
                return None, None

            col = self.detecter_colonne_avis(df)
            df_res = self.analyseur.analyser_batch(df, col)
            
            if df_res.empty:
                return None, None

            out_path = output_dir / f"analyse_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            df_res.to_excel(out_path, index=False)
            return df_res, out_path
        except Exception as e:
            print(f"Erreur lors de l'analyse: {e}")
            raise e