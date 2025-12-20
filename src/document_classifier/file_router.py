from pathlib import Path


BASE_DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def save_file_by_class(uploaded_file, predicted_class: str):
    target_dir = BASE_DATA_DIR / predicted_class.lower()
    target_dir.mkdir(parents=True, exist_ok=True)

    file_path = target_dir / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path
