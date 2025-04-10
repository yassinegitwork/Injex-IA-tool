import json
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

def train_model():
    try:
        with open('scan_report.json', 'r') as f:
            data = json.load(f)
        
        # Create combined labels: vulnerability_type_risk_level (e.g., "XSS_high", "SQLi_medium")
        labels = [f"{entry['vulnerability']}_{entry.get('risk', 'medium')}" for entry in data["vulnerabilities"]]
        
        # Extract payloads
        payloads = [entry["payload"] for entry in data["vulnerabilities"]]

        # Vectorize the payloads using CountVectorizer
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(payloads).toarray()
        y = np.array(labels)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a RandomForestClassifier
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)

        # Evaluate model accuracy
        accuracy = accuracy_score(y_test, clf.predict(X_test))
        print(f"[+] Model Accuracy: {accuracy * 100:.2f}%")

        # Save the trained model and vectorizer
        joblib.dump(clf, 'vulnerability_model.pkl')
        joblib.dump(vectorizer, 'vectorizer.pkl')
        print("[+] Model and vectorizer saved successfully.")

        # ✅ Save vectorizer vocabulary to txt
        with open('vectorizer_vocab.txt', 'w', encoding='utf-8') as f:
            f.write("Vectorizer Vocabulary:\n")
            for word, index in vectorizer.vocabulary_.items():
                f.write(f"{word}: {index}\n")
        print("[+] Saved vectorizer_vocab.txt")

        return accuracy

    except Exception as e:
        print(f"[!] Auto-train failed: {e}")
        return None
