import streamlit as st
import json
import os

# Carregar dados
@st.cache_data
def load_classes():
    with open("data/classes.json", "r", encoding="utf-8") as f:
        return json.load(f)

classes = load_classes()

# Sidebar
st.sidebar.title("Evil Hunter Tycoon")
classe_nomes = [c["nome"] for c in classes]
classe_escolhida = st.sidebar.selectbox("Escolha uma classe:", classe_nomes)

# Conteúdo
classe = next(c for c in classes if c["nome"] == classe_escolhida)

st.title(f"Classe: {classe['nome']}")
st.markdown(f"📝 **Descrição:** {classe['descricao']}")
st.markdown("🎯 **Funções principais:**")
st.markdown("- " + "\n- ".join(classe["funcoes"]))

if classe.get("subclasses"):
    st.markdown("🧬 **Subclasses:**")
    st.markdown("- " + "\n- ".join(classe["subclasses"]))

# Mostrar imagem
img_path = os.path.join("assets", "imagens_das_classes", classe["imagem"])
if os.path.exists(img_path):
    st.image(img_path, width=300)
else:
    st.warning("Imagem não encontrada.")

