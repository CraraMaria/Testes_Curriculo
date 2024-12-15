import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Maria Clara Fontenele Silva",
    page_icon="🍓",
    layout="centered",
    initial_sidebar_state="auto"
)

# Tabulação
tab1, tab2 = st.tabs(["Currículo", "Outros Conteúdos"])

with tab1:
    # Colunas dentro da aba 1
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("Maria Clara Fontenele Silva")
        st.write("Estudante de Ciência da Computação. Desenvolvimento de Software e Interesse em Ciência de Dados.")
        st.write("Experiência de trabalho em empresa de Desenvolvimento. Experiência de projetos acadêmicos.")
        
        st.divider()
        st.subheader(":blue[EXPERIÊNCIA PROFISSIONAL]")
        st.write("**BENU SISTEMAS ERP - Desenvolvimento de Software**")
        st.caption("O BENU é um sistema ERP, projetado para otimizar a gestão de recursos e processos nas empresas. Software de Gestão Online Completo Para Controladoras de Pragas")
        st.write("**Cargo: Suporte a Software (Estágio)**")
        st.caption("""
- Prestava Suporte Técnico para o software ERP, auxiliando usuários na resolução de problemas e dúvidas operacionais;
- Identificar e reportar bugs ao time de desenvolvimento, contribuindo para a melhoria contínua do sistema:
- Colaborava com o time de desenvolvimento na correção de erros e melhorias do sistema;
- Fazia a construção de base de conhecimento do sistema;

""")

        
        st.divider()
        st.subheader(":blue[PROJETOS]")
        st.write("**[Projeto condomínio New Garden](https://github.com/CraraMaria/centroautomotivo)** — _Projeto de Programação Orientada a Objetos_")
        st.caption("Este projeto consiste em um aplicativo voltado para a gestão de condomínios, com funcionalidades para reserva de áreas comuns, comunicação entre moradores e administração.")
        st.write("**[Projeto Currículo](https://curriculodoc-clara.streamlit.app)** — _Projeto Python_")
        st.caption("Criação deste currículo interativo usando Streamlit.")
        st.write("**Projeto Guia do Universitário** — _Projeto Integrador_")
        st.caption("Solução prática para calouros, com dicas sobre a faculdade e contratação de monitores.")


        st.divider()
        st.subheader(":blue[CERTIFICAÇÃO EM INGLÊS]")
        st.write("Curso Pleno de Língua Estrangeira Moderna Inglês — **Concluído em 2017**")
        st.caption("Centro Interescolar de Línguas do GAMA")

        st.divider()
        st.subheader(":blue[FORMAÇÃO]")
        st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
        st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")

        st.divider()

        st.subheader(":blue[REDES]")

        button_col1, button_col2, button_col3, button_col4 = st.columns([1, 1, 1, 1])

        with button_col1:
            st.link_button("🐱 Github", "https://github.com/CraraMaria") 

        with button_col2:
            st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/maria-clara-fontenele-silva-334a08292/")
          
        with button_col3:
            st.link_button(" 📝 Medium", "https://medium.com/@fontenelesilvamariaclara")
          
        with button_col4:
            st.link_button("🌊 Overflow", "https://stackoverflow.com/users/27588517/maria-clara-fontenele-silva?tab=topactivity")


    with col2:
        st.caption("Santa Maria, DF, 72594-235")
        st.caption("**☎️ +55 61 98160-7950**")
        st.caption("**fontenelesilvamariaclara@gmail.com**")
        st.caption("**maria.silva27@iesb.edu.br**")
        
        st.divider()
        st.write(":blue[COMPETÊNCIAS]")
        st.caption("Programação: C, Java, Python.")
        st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
        st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
        st.caption("Ferramentas: Eclipse, Visual Studio Code, Spring Boot.")
        st.caption("Gestão de Projetos: Scrum, Kanban, Microsoft Project, Trello, Jira.")
        st.caption("Pacote Office: Word, Excel, PowerPoint.")
        st.caption("Sistemas Operacionais: Linux, Windows.")

        st.divider()
        st.write(":blue[PROJETOS VOLUNTÁRIOS]")
        st.caption("Monitoria em Geometria Analítica e Lógica Matemática.")
        st.caption("Apoio na organização e aplicação de provas para o EAD.")
        
        st.divider()
        st.write(":blue[IDIOMAS]")
        st.caption("Língua Moderna Inglês avançado.")


st.divider()

# URL do arquivo PDF no GitHub
pdf_url = "https://raw.githubusercontent.com/CraraMaria/Testes_Currículo/main/Currículo_ClaraFontenele.pdf"  # Atualize com o link correto

# Cria o botão de download
st.markdown(f'<a href="{pdf_url}" download="Currículo_ClaraFontenele.pdf">Baixar em PDF</a>', unsafe_allow_html=True)

with tab2:
    # Conteúdo para a aba 2
    # tentar colocar foto interativa
    st.write("PÁGINA EM CONSTRUÇÃO 🛠👩‍🚒")
    st.write("Mais sobre mim")
    st.image("fotodeperfil.png", caption="Clara Fontenele", width=200)
    st.title("Sobre Mim")
    st.write("""
Sou Maria Clara Fontenele Silva, uma estudante apaixonada por resolver problemas com tecnologia e sempre em busca de aprender algo novo. 
Meu objetivo é me tornar uma desenvolvedora de destaque, com interesse especial em Ciência de Dados e Desenvolvimento Full Stack. 
Além da tecnologia, gosto de [seu hobby, como leitura, música, etc.].
""")
    st.title("Projetos")
    st.subheader("Projeto Currículo")
    st.write("""
Este é um projeto feito com Streamlit, onde criei um currículo interativo para treinar minhas habilidades de desenvolvimento web. 
[Veja o código no GitHub](#)
""")
    st.title("Contato")
with st.form(key='contact_form'):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    message = st.text_area("Mensagem")
    submit = st.form_submit_button("Enviar")
    if submit:
        st.success("Mensagem enviada com sucesso!")
    
