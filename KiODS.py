import streamlit as st

def show_main_page():
    st.title("KiODS - Análise de ODS para Iniciativas Sustentáveis")

    odss_analysis()

def main():
    st.sidebar.image("logoesg.png", use_column_width=True, caption="PDI Ceneged")
    st.sidebar.title("Menu")
    menu_options = ["Análise", "Sobre", "Recursos", "Dados"]
    choice = st.sidebar.selectbox("Escolha uma opção", menu_options)

    if choice == "Análise":
        show_main_page()
    elif choice == "Sobre":
        show_about_page()
    elif choice == "Recursos":
        show_resources_page()
    elif choice == "Dados":
        show_statistics_page()

def show_about_page():
    st.title("Sobre")
    st.write(
        "O KIODS é um aplicativo intuitivo e acessível, projetado para auxiliar iniciativas e projetos a avaliar seu impacto em relação aos Objetivos de Desenvolvimento Sustentável (ODS) da ONU. Com uma interface simples e interativa, o aplicativo orienta os usuários por meio de perguntas específicas relacionadas a cada ODS, ajudando-os a entender quais metas de sustentabilidade estão sendo atendidas por suas ações.")

def show_resources_page():
    st.title("Recursos")
    st.write("Aqui estão alguns recursos úteis para ajudar na compreensão e implementação dos ODS:")

    st.markdown("- [Site oficial dos Objetivos de Desenvolvimento Sustentável](https://sdgs.un.org/)")
    st.markdown("- [Fórum IST](https://sdgs.un.org/tfm/sti-forum)")
    st.markdown("- [Publicações](https://sdgs.un.org/publications)")

def show_statistics_page():
    st.title("Dados")
    st.write("De acordo com Organização das Nações Unidas (ONU):")

    st.markdown("- Existem 17 Objetivos de Desenvolvimento Sustentável, cada um com metas específicas. Eles abrangem áreas como erradicação da pobreza, saúde, educação, igualdade de gênero, água limpa, energia acessível, trabalho decente, inovação e muitos outros aspectos do desenvolvimento sustentável.")
    st.markdown("- As metas das ODS estão programadas para serem alcançadas até 2030, o que enfatiza a urgência de agir para abordar os desafios globais.")
    st.markdown("- As ODS envolvem uma ampla participação de governos, setor privado, sociedade civil e cidadãos. A colaboração internacional é fundamental para alcançar esses objetivos.")
    st.markdown("- Mais de 1 bilhão de pessoas em todo o mundo vivem com deficiências")
    st.markdown("- As mudanças climáticas, a perda de biodiversidade e a degradação ambiental são desafios globais abordados pelas ODS, com foco especial na ação climática (ODS 13) e vida submarina e terrestre (ODS 14 e ODS 15).")
    st.markdown("- Em todo o mundo, 617 milhões de crianças e adolescentes não atingiram níveis mínimos de proficiência em leitura e matemática.")
    st.markdown("- Em 2017, 2,1 bilhões de pessoas em todo o mundo não tinham acesso a água potável em casa.")

def odss_analysis():
    odss = [
        "1. Erradicar a pobreza",
        "2. Fome zero e agricultura sustentável",
        "3. Saúde e bem-estar",
        "4. Educação de qualidade",
        "5. Igualdade de gênero",
        "6. Água potável e saneamento",
        "7. Energia limpa e acessível",
        "8. Trabalho decente e crescimento econômico",
        "9. Indústria, inovação e infraestrutura",
        "10. Redução das desigualdades",
        "11. Cidades e comunidades sustentáveis",
        "12. Consumo e produção responsáveis",
        "13. Ação contra a mudança global do clima",
        "14. Vida na água",
        "15. Vida terrestre",
        "16. Paz, justiça e instituições eficazes",
        "17. Parcerias e meios de implementação"
    ]

    perguntas = [
        "Sua iniciativa contribui para diminuir ou acabar com a pobreza?",  # 1
        "Sua iniciativa de alguma forma promove o fim da fome ou incentivo a uma agricultura sustentável? ",  # 2
        "Sua iniciativa de alguma forma busca incentivar uma vida saudável e promover o bem-estar para todas e todos, em todas as idades?",  # 3
        "Sua iniciativa contribui para proporcionar educação?",  # 4
        "Sua iniciativa promove a igualdade de gênero ou busca empoderar as mulheres e meninas?",  # 5
        "Ações estão sendo tomadas para garantir água potável e saneamento? Garantindo disponibilidade e gestão sustentável da água e saneamento!",  # 6
        "Sua iniciativa promove energia limpa e acessível? Busca promover acesso confiável, sustentável, moderno e a preço acessível à energia?",  # 7
        "Na sua iniciativa se busca promover o crescimento econômico sustentado, inclusivo e sustentável, geração de emprego pleno e produtivo e trabalho decente?",  # 8
        "Sua iniciativa visa construir infraestruturas resilientes, promover a industrialização inclusiva e sustentável ou fomentar a inovação?",  # 9
        "Sua iniciativa contribui para a redução das desigualdades?",  # 10
        "Ações estão sendo tomadas para tornar as ruas, bairros, cidades ou assentamentos humanos inclusivos, seguros, resilientes e sustentáveis?",  # 11
        "Sua iniciativa promove consumo e produção responsáveis?",  # 12
        "Sua iniciativa visa combater a mudança climática e seus impactos?",  # 13
        "Sua iniciativa contribui para a conservação e uso sustentável dos oceanos, dos mares e dos recursos marinhos para o desenvolvimento sustentável?",  # 14
        "Ações estão sendo tomadas para proteger, recuperar e promover o uso sustentável dos ecossistemas terrestres, gerir de forma sustentável as florestas, combater a desertificação, deter e reverter a degradação da terra e deter a perda de biodiversidade?",  # 15
        "Sua iniciativa visa promover sociedades pacíficas e inclusivas para o desenvolvimento sustentável, proporcionar o acesso à justiça para todos e construir instituições eficazes, responsáveis e inclusivas em todos os níveis?",  # 16
        "Sua iniciativa visa fortalecer os meios de implementação e revitalizar a parceria global ou local para o desenvolvimento sustentável?"  # 17

    ]

    pesos = [2, 1, 3, 3, 1, 2, 3, 3, 3, 2, 3, 1, 3, 2, 2, 2, 3]
    pontuacao_total = 0
    odss_atendidas = []

    for ods, pergunta, peso in zip(odss, perguntas, pesos):
        resposta = st.radio(pergunta, ['Não', 'Sim'])
        if resposta == 'Sim':
            pontuacao_total += peso
            odss_atendidas.append(ods)

    if st.button("Ver Resultados"):
        mostrar_resultados(odss_atendidas, pontuacao_total)

def mostrar_resultados(odss_atendidas, pontuacao_total):
    st.markdown(
        f"\n**Pontuação Total:** {pontuacao_total}")

    st.markdown("\n**As ODS's que sua iniciativa atende são:**")
    for ods in odss_atendidas:
        st.markdown(f"- {ods}")

if __name__ == "__main__":
    main()

st.markdown("---")
st.markdown("Desenvolvido por [PedroFS](https://linktr.ee/Pedrofsf)")
