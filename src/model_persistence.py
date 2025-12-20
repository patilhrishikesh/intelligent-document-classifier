import joblib
from pathlib import Path

ARTIFACTS_DIR = Path('artifacts')
ARTIFACTS_DIR.mkdir(exist_ok = True)

def save_artifact(obj, filename: str) -> None:
    
    path = ARTIFACTS_DIR / filename
    joblib.dump(obj, path)
    
def load_artifact(filename: str):
    # load a saved python object from disk
    
    path = ARTIFACTS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Artifacts not found :{path}")

    return joblib.load(path)
    
