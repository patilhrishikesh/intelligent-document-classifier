from pathlib import Path
from typing import List, Tuple

def load_raw_documents(data_dir: str) -> Tuple[List[str], List[str]]:
    
    """
    Load raw text documents from directory structure.add()

    Args:
        data_dir (str): Path to raw data directory.

    Returns:
        texts (List[str]): List of documeent texts.
        labels (List[str]): corresponding document labels.
    """
    texts = []
    labels = []

    base_path = Path(data_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for category_dir in base_path.iterdir():
        if not category_dir.is_dir():
            continue

        label = category_dir.name

        for file_path in category_dir.glob("*.txt"):
            try:
                # Try UTF-8 first
                content = file_path.read_text(encoding="utf-8").strip()

            except UnicodeDecodeError:
                # Fallback for Windows / special encodings
                content = file_path.read_text(encoding="latin-1").strip()

            if not content:
                print(f"[SKIPPED EMPTY] {file_path}")
                continue

            texts.append(content)
            labels.append(label)

    return texts, labels
