import joblib
from pathlib import Path

<<<<<<< HEAD
ARTIFACTS_DIR =  Path(__file__).resolve().parents[2] / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok = True)
=======
# Absolute, OS-independent path to project-root/artifacts
ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok=True)

>>>>>>> 3bf4e96538d915689f74871a750f1ade31bfdf7e

def save_artifact(obj, filename: str) -> None:
    path = ARTIFACTS_DIR / filename
    joblib.dump(obj, path)


def load_artifact(filename: str):
    path = ARTIFACTS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Artifacts not found: {path}")
    return joblib.load(path)
