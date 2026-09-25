from pathlib import Path
import yaml


def load_config():
    config_path = Path(__file__).resolve().parent.parent / "config" / "settings.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
