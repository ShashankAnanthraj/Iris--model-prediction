from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

def main():
    data = load_iris()
    X = data['data']
    y = data['target']
    class_names = data['target_names'].tolist()

    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=200, n_jobs=None))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipe.fit(X_train, y_train)
    acc = accuracy_score(y_test, pipe.predict(X_test))
    print(f"Test accuracy: {acc:.3f}")

    joblib.dump({
        "model": pipe,
        "class_names": class_names
    }, "model.joblib")

if __name__ == "__main__":
    main()
