import streamlit as st
import pandas as pd
import json
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path

@st.cache_data
def load_file(file_path: str):
    ext = Path(file_path).suffix.lower()

    with open(file_path, "r", encoding="utf-8") as f:
        if ext == ".yaml" or ext == ".yml":
            return yaml.safe_load(f)
        elif ext == ".json":
            return json.load(f)
        elif ext == ".csv":
            return pd.read_csv(f)
        elif ext == ".xml":
            tree = ET.parse(f)
            return tree.getroot()  # ou você pode converter para dict se quiser
        else:
            raise ValueError(f"Extensão de arquivo não suportada: {ext}")