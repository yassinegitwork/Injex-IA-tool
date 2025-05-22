import json
import joblib
import numpy as np
import os
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report
)

def train_model(filter_type=None):
    try:
        with open('scan_report.json', 'r') as f:
            data = json.load(f)

        entries = data["vulnerabilities"]

        # Filter entries by vulnerability type if specified
        if filter_type:
            entries = [entry for entry in entries if entry["vulnerability"] == filter_type]

        if not entries:
            print(f"[!] No entries found for type '{filter_type}'. Skipping training.")
            return None

        labels = [f"{entry['vulnerability']}_{entry.get('risk', 'medium')}" for entry in entries]
        payloads = [entry["payload"] for entry in entries]

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(payloads).toarray()
        y = np.array(labels)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)

        # Use only labels present in this filtered dataset
        used_labels = sorted(set(y))  # only labels that actually appear in this scan

        # Compute metrics using filtered labels
        accuracy = accuracy_score(y_test, y_pred)
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average='weighted', zero_division=0
        )

        report = classification_report(
            y_test, y_pred,
            labels=used_labels,
            output_dict=True,
            zero_division=0
        )


        # Save model and vectorizer
        joblib.dump(clf, 'vulnerability_model.pkl')
        joblib.dump(vectorizer, 'vectorizer.pkl')
        print("[+] Model and vectorizer saved successfully.")

        # Save vectorizer vocabulary
        with open('vectorizer_vocab.txt', 'w', encoding='utf-8') as f:
            f.write("Vectorizer Vocabulary:\n")
            for word, index in vectorizer.vocabulary_.items():
                f.write(f"{word}: {index}\n")
        print("[+] Saved vectorizer_vocab.txt")

        # Save metrics to metrics.json
        metrics_entry = {
            "timestamp": datetime.now().isoformat(),
            "filter_type": filter_type,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "labels": used_labels,
            "classification_report": report
        }

        metrics_file = "metrics.json"
        existing_metrics = []
        if os.path.exists(metrics_file) and os.path.getsize(metrics_file) > 0:
            try:
                with open(metrics_file, "r") as f:
                    existing_metrics = json.load(f)
            except json.JSONDecodeError:
                print("[!] Warning: metrics.json is invalid. Starting fresh.")

        existing_metrics.append(metrics_entry)

        with open(metrics_file, "w") as f:
            json.dump(existing_metrics, f, indent=4)

        print("[+] Saved and updated metrics.json")

    except Exception as e:
        print(f"[!] Auto-train failed: {e}")
        return None
