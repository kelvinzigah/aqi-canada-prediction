import joblib
from sklearn.model_selection import train_test_split
from src.config import TEST_SIZE, RANDOM_STATE, MODELS_DIR
from src.load_data import load_processed
from src.preprocessing import run as preprocess
from src.models import get_models


def train_all() -> dict:
    df = load_processed()
    X, y = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    trained = {}
    for name, model in get_models().items():
        model.fit(X_train, y_train)
        trained[name] = {"model": model, "X_test": X_test, "y_test": y_test}

    best_name = min(trained, key=lambda n: trained[n]["model"].score(
        trained[n]["X_test"], trained[n]["y_test"]
    ))
    joblib.dump(trained[best_name]["model"], MODELS_DIR / "saved_model.pkl")
    print(f"Best model: {best_name} — saved to models/saved_model.pkl")
    return trained


if __name__ == "__main__":
    train_all()
