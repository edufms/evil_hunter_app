import streamlit as st
import json
import os
import utils.load_data

# Carregar dados
classes = load_data.load_classes('utils/classes.yaml')

# Título do app
st.title("Evil Hunter Tycoon - Guia de Classes")
st.markdown("Explore as classes, subclasses e habilidades da 3ª classe.")

# Seletor de classe
classe_nomes = [classe["nome"] for classe in classes]
escolhida = st.selectbox("Escolha uma classe:", classe_nomes)

# Encontrar a classe selecionada
classe_info = next((c for c in classes if c["nome"] == escolhida), None)

if classe_info:
    st.header(classe_info["nome"])
    #st.image(classe_info["imagem"], width=200)
    st.markdown(f"**Descrição:** {classe_info['descricao']}")
    st.markdown(f"**Funções:** {', '.join(classe_info['funcoes'])}")

    if "requisitos" in classe_info:
        req = classe_info["requisitos"]
        st.markdown("**Requisitos:**")
        st.markdown(f"- Nível mínimo: {req.get('nivel_minimo', '-')}")
        st.markdown(f"- Itens necessários: {', '.join(req.get('itens_necessarios', []))}")

    if "builds" in classe_info:
        st.markdown("**Builds Sugeridas:**")
        for build in classe_info["builds"]:
            st.markdown(f"- **{build['nome']}**: {build['descricao']}")
            st.markdown(f"  - Atributos: {', '.join(build['atributos'])}")
            st.markdown(f"  - Equipamentos: {', '.join(build['equipamentos'])}")

    if "utilidades" in classe_info:
        st.markdown(f"**Utilidades:** {', '.join(classe_info['utilidades'])}")

    if "subclasses" in classe_info:
        st.subheader("Subclasses:")
        for sub in classe_info["subclasses"]:
            st.markdown(f"### {sub['nome']}")
            st.image(sub["imagem"], width=150)
            st.markdown(f"**Descrição:** {sub['descricao']}")
            st.markdown(f"**Funções:** {', '.join(sub['funcoes'])}")

            if sub.get("habilidades_3a_classe"):
                st.markdown("**Habilidades da 3ª Classe:**")
                for hab in sub["habilidades_3a_classe"]:
                    st.markdown(f"- **{hab['nome']}**: {hab['descricao']}")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por fãs para a comunidade de Evil Hunter Tycoon")
