import json
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text

def train_model():
    # Load the scan_report.json file
    with open('scan_report.json', 'r') as f:
        data = json.load(f)

    # Extract data from the report
    payloads = [entry["payload"] for entry in data["vulnerabilities"]]
    vulnerabilities = [entry["vulnerability"] for entry in data["vulnerabilities"]]

    # Convert payloads to feature vectors
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(payloads).toarray()
    y = np.array(vulnerabilities)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Evaluate accuracy
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"[+] Model Accuracy: {accuracy * 100:.2f}%")

    # Save the model and vectorizer
    joblib.dump(clf, 'vulnerability_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    print("[+] Model and vectorizer saved successfully.")

    # === Export Model Info to Text Files ===
    # Vectorizer vocabulary
    with open('vectorizer_vocab.txt', 'w', encoding='utf-8') as f:
        f.write("Vectorizer Vocabulary:\n")
        for word, index in vectorizer.vocabulary_.items():
            f.write(f"{word}: {index}\n")
    print("[+] Saved vectorizer_vocab.txt")

   
# Run the function to train the model
train_model()
