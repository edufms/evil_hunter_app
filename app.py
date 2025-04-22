import streamlit as st
import json
import os

# Carregar dados
@st.cache_data
def load_classes():
    with open("/app/nome-do-seu-repo/classes.json", "r", encoding="utf-8") as f:
        return json.load(f)

classes = load_classes()

# Sidebar
st.sidebar.title("Evil Hunter Tycoon")
classe_nomes = [c["nome"] for c in classes]
classe_escolhida = st.sidebar.selectbox("Escolha uma classe:", classe_nomes)

# Conteúdo
classe = next(c for c in classes if c["nome"] == classe_escolhida)

classe = st.selectbox("Escolha uma classe", [c["nome"] for c in classes])

classe_info = next(c for c in classes if c["nome"] == classe)
st.markdown(f"### {classe_info['descricao']}")

for sub in classe_info["subclasses"]:
    st.markdown(f"#### Subclasse: {sub['nome']}")
    st.markdown(f"Descrição: {sub['descricao']}")
    for hab in sub.get("habilidades_3a_classe", []):
        st.markdown(f"- **{hab['nome']}**: {hab['descricao']}")

st.title(f"Classe: {classe['nome']}")
st.markdown(f"📝 **Descrição:** {classe['descricao']}")
st.markdown("🎯 **Funções principais:**")
st.markdown("- " + "\n- ".join(classe["funcoes"]))

if classe.get("subclasses"):
    st.subheader("🧬 Subclasses")
    for sub in classe["subclasses"]:
        st.markdown(f"### {sub['nome']}")
        st.markdown(f"📝 {sub['descricao']}")
        st.markdown("🎯 **Funções:**")
        st.markdown("- " + "\n- ".join(sub["funcoes"]))
        sub_img_path = os.path.join("assets", "imagens_das_classes", sub["imagem"])
        if os.path.exists(sub_img_path):
            st.image(sub_img_path, width=250)
        st.markdown("---")


# Mostrar imagem
img_path = os.path.join("assets", "imagens_das_classes", classe["imagem"])
if os.path.exists(img_path):
    st.image(img_path, width=300)
else:
    st.warning("Imagem não encontrada.")

