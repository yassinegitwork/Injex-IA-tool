# train_model.py
import json
import joblib
import numpy as np
import os
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix
)

def train_model():
    try:
        with open('scan_report.json', 'r') as f:
            data = json.load(f)

        labels = [f"{entry['vulnerability']}_{entry.get('risk', 'medium')}" for entry in data["vulnerabilities"]]
        payloads = [entry["payload"] for entry in data["vulnerabilities"]]

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(payloads).toarray()
        y = np.array(labels)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)

        # === Metrics ===
        accuracy = accuracy_score(y_test, y_pred)
        precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
        report = classification_report(y_test, y_pred, output_dict=True)
        conf_matrix = confusion_matrix(y_test, y_pred)

        print(f"[+] Accuracy: {accuracy * 100:.2f}%")

        # === Pretty Confusion Matrix Display ===
        labels_sorted = sorted(list(set(y)))
        conf_df = pd.DataFrame(conf_matrix, index=labels_sorted, columns=labels_sorted)

        print("\nConfusion Matrix:\n")
        print(conf_df.to_string())

        # === Save Confusion Matrix to Markdown File ===
        with open("confusion_matrix.md", "w") as f:
            f.write("# Confusion Matrix\n\n")
            f.write(conf_df.to_markdown())
        print("[+] Confusion matrix saved as 'confusion_matrix.md'")

        # === Save Model and Vectorizer ===
        joblib.dump(clf, 'vulnerability_model.pkl')
        joblib.dump(vectorizer, 'vectorizer.pkl')
        print("[+] Model and vectorizer saved successfully.")

        # === Save Vocabulary ===
        with open('vectorizer_vocab.txt', 'w', encoding='utf-8') as f:
            f.write("Vectorizer Vocabulary:\n")
            for word, index in vectorizer.vocabulary_.items():
                f.write(f"{word}: {index}\n")
        print("[+] Saved vectorizer_vocab.txt")

        # === Save All Metrics to metrics.json ===
        metrics_entry = {
            "timestamp": datetime.now().isoformat(),
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "labels": labels_sorted,
            "classification_report": report,
            "confusion_matrix": conf_matrix.tolist()
        }

        metrics_file = "metrics.json"
        if os.path.exists(metrics_file):
            with open(metrics_file, "r") as f:
                existing_metrics = json.load(f)
        else:
            existing_metrics = []

        existing_metrics.append(metrics_entry)

        with open(metrics_file, "w") as f:
            json.dump(existing_metrics, f, indent=4)

        print("[+] Saved and updated metrics.json")

        return accuracy

    except Exception as e:
        print(f"[!] Auto-train failed: {e}")
        return None
