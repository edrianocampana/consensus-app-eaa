import streamlit as st
import openai

# Configuração da página
st.set_page_config(page_title="Detector + Consensus", layout="wide")
st.title("🔬 Analisador de Discurso Negacionista sobre EAA + Consulta ao Consensus")

# ✅ A chave é carregada de forma segura via .streamlit/secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Entrada do usuário
user_input = st.text_area("✍️ Cole aqui o discurso a ser analisado", height=300)

# Botão de análise
if st.button("🔍 Analisar e Buscar Evidência"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, insira um discurso para análise.")
    else:
        with st.spinner("Gerando pergunta científica..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Você é um cientista que formula perguntas científicas a partir de discursos negacionistas sobre esteroides anabolizantes (EAA)."},
                    {"role": "user", "content": f"Discurso: {user_input}"}
                ]
            )
            question = response.choices[0].message["content"]
            st.success("✅ Pergunta científica gerada!")
            st.write(f"**Pergunta:** {question}")

        st.markdown("---")
        st.subheader("📚 Resultado da busca (simulada) no Consensus:")
        st.info("Nesta versão simplificada, recomendamos copiar a pergunta acima e colar manualmente em [consensus.app](https://consensus.app).")
        search_url = f"https://consensus.app/search?q={question.replace(' ', '+')}"
        st.markdown(f"[🔗 Clique aqui para buscar no Consensus]({search_url})")
