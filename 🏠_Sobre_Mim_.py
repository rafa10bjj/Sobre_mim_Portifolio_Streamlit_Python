# ══════════════════════════════════════════════════════════════════════
# IMPORTAÇÕES - Bibliotecas necessárias para o funcionamento do app
# ══════════════════════════════════════════════════════════════════════
import streamlit as st  # Framework principal para criar o app web
import base64           # Para converter imagens locais em base64 (necessário no Streamlit)

# ══════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DA PÁGINA
# Deve ser o PRIMEIRO comando Streamlit do arquivo
# ══════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Portfólio - Rafael Rodrigues",  # Título que aparece na aba do navegador
    page_icon="🚀",                              # Ícone da aba do navegador
    layout="wide",                              # Layout largo (usa toda a largura da tela)
    initial_sidebar_state="expanded"            # Sidebar começa ABERTA ao carregar a página
)

# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: CONVERTER IMAGEM LOCAL PARA BASE64
# O Streamlit não carrega imagens locais direto no HTML por segurança.
# Convertemos a imagem para uma string base64 que o navegador entende.
# ══════════════════════════════════════════════════════════════════════
def get_img_base64(path):
    """
    Recebe o caminho de uma imagem (ex: 'img/foto.jpeg')
    e retorna uma string no formato: data:image/jpeg;base64,XXXXX
    que pode ser usada diretamente no atributo src de uma tag <img>
    """
    try:
        with open(path, "rb") as f:                          # Abre o arquivo em modo binário
            ext = path.split(".")[-1].lower()                # Pega a extensão do arquivo (jpg, png...)
            mime = "jpeg" if ext in ["jpg", "jpeg"] else ext # Define o tipo MIME correto
            b64 = base64.b64encode(f.read()).decode()         # Converte para base64 e decodifica para string
            return f"data:image/{mime};base64,{b64}"          # Retorna o formato aceito pelo HTML
    except FileNotFoundError:
        st.warning(f"Arquivo não encontrado: {path}")
        return ""  # Retorna string vazia se o arquivo não existir (evita crash)
    except Exception as e:
        st.error(f"Erro ao carregar a imagem {path}: {e}")
        return ""

# ══════════════════════════════════════════════════════════════════════
# PRÉ-CARREGAMENTO DAS IMAGENS
# Carregamos todas as imagens em base64 no início para não repetir
# a função a cada renderização da página
# ══════════════════════════════════════════════════════════════════════
foto_perfil = get_img_base64("img/img01.png")   # Foto do perfil da sidebar
foto_sobre  = get_img_base64("img/img02.png")   # Foto da seção Sobre Mim

# Verifica se as imagens foram carregadas corretamente
if not foto_perfil:
    st.error("Erro ao carregar a imagem de perfil. Verifique se o arquivo 'img/img01.png' existe.")
if not foto_sobre:
    st.error("Erro ao carregar a imagem da seção Sobre Mim. Verifique se o arquivo 'img/img02.png' existe.")

# ══════════════════════════════════════════════════════════════════════
# DADOS DO PORTFÓLIO
# Centralizamos todos os dados aqui para facilitar edição futura.
# Basta alterar estes dicionários para atualizar o conteúdo do site.
# ══════════════════════════════════════════════════════════════════════

# --- HABILIDADES TÉCNICAS ---
# Dicionário onde a chave é o título da categoria e o valor é uma lista de habilidades
SKILLS = {
    "📊 Dados & BI": [
        "Power BI (DAX, Power Query)",
        "SQL Server",
        "Python (Pandas, Matplotlib)",
        "Excel Avançado / VBA",
        "Design de Dashboards",
        "Data Storytelling",
        "AI Generativa"
    ],
    "💻 Gestão de Pessoas": [
        "Liderança de Equipes",
        "Gestão de Conflitos",
        "Processos e Indicadores",
    ],
    "🚛 Logística": [
        "Supply Chain",
        "Gestão de Estoque / WMS",
        "Planejamento de Demanda",
        "Gestão de Frotas",
        "Roteirização",
    ]
}

# --- EXPERIÊNCIA PROFISSIONAL ---
# Ordem cronológica DECRESCENTE (mais recente primeiro) conforme PDF do currículo
EXPERIENCE = [
    {
        "titulo":  "Analista de Prevenção e Demanda",
        "empresa": "Kiosk Brands — Intelligence & Supply Chain",
        "periodo": "Janeiro/2026 – Atual",
        "icon":    "📊",  # Ícone visual para identificar rapidamente a experiência
        "resultados": [
            "Desenvolvimento de dashboards em Power BI para monitoramento de KPIs",
            "Automação de rotinas de cotação via scripts em Python",
            "Gestão de ciclo de compras end-to-end com foco em insumos críticos",
            "Análise de dados operacionais para identificação de oportunidades de otimização",
        ],
        "atividades": [
            "Desenvolver dashboards em Power BI para performance de fornecedores",
            "Automatizar rotinas de cotação e tratamento de bases de dados com Python",
            "Gerenciar ciclo de compras desde sourcing até aquisição",
            "Analisar dados operacionais para otimização de processos",
            "Suporte a decisões estratégicas com inteligência de dados",
        ]
    },
    {
        "titulo":  "Encarregado de Logística",
        "empresa": "Fattu do Brasil",
        "periodo": "Agosto/2022 – Novembro/2025",
        "icon":    "🚛",
        "resultados": [
            "Melhoria do processo de acompanhamento das tarefas da equipe",
            "Otimização da liberação de veículos através da análise dos dados operacionais",
            "Otimização do processo de inventário",
            "Gestão eficiente para manter clima corporativo saudável",
        ],
        "atividades": [
            "Análise de Dados dos Processos Logísticos",
            "Distribuir e acompanhar o desempenho das tarefas da equipe",
            "Controlar jornada, folha de ponto e gestão diária da equipe",
            "Controle do Estoque – Armazenagem e Recebimento",
            "Mapeamento de Processos de Inventário",
            "Transporte, Roteirização e Monitoramento de Entregas",
            "Geração de Relatórios e Dashboards para suporte à gerência",
            "Liderança de Equipe e Gestão de Pessoas",
        ]
    },
    {
        "titulo":  "Encarregado Geral",
        "empresa": "Focus Distribuidora Ltda",
        "periodo": "Agosto/2009 – Maio/2019",
        "icon":    "📦",
        "resultados": [
            "Liderança da equipe operacional por quase uma década",
            "Implementação de melhorias nos processos de inventário e armazenagem com WMS",
            "Geração de relatórios operacionais e análises para suporte à gerência",
            "Padronização de processos internos do armazém",
        ],
        "atividades": [
            "Liderar equipe operacional e gestão geral de armazém",
            "Implementar melhorias nos processos de inventário utilizando WMS",
            "Gerar relatórios operacionais e análises gerenciais",
            "Controle de estoque, recebimento e expedição",
            "Gestão de documentação fiscal e controle de entregas",
            "Treinamento e desenvolvimento de colaboradores",
        ]
    },
]

# --- FORMAÇÃO ACADÊMICA ---
# Lista em ordem decrescente (mais recente primeiro) conforme PDF
EDUCATION = [
    {
        "curso":       "Análise e Desenvolvimento de Sistemas",
        "instituicao": "Unifatécio",
        "periodo":     "Dezembro/2025 – Em andamento",
        "icon":        "🎓",
        "status":      "andamento"   # Controla qual badge mostrar (verde ou ciano)
    },
    {
        "curso":       "Python Impressionador",
        "instituicao": "Hashtag Treinamentos",
        "periodo":     "Janeiro/2024 – Em andamento",
        "icon":        "🐍",
        "status":      "andamento"
    },
    {
        "curso":       "Formação em Análise de Dados",
        "instituicao": "Xperiun Data Analytics",
        "periodo":     "Concluído",
        "icon":        "📊",
        "status":      "concluido"
    },
    {
        "curso":       "MBA em Logística Empresarial",
        "instituicao": "Estácio",
        "periodo":     "Março/2023 – Março/2024",
        "icon":        "🏫",
        "status":      "concluido"
    },
    {
        "curso":       "Gestão da Cadeia de Suprimentos",
        "instituicao": "UNIP",
        "periodo":     "Janeiro/2021 – Dezembro/2023",
        "icon":        "🚚",
        "status":      "concluido"
    },
]

# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: CARREGAR CSS
# Todo o estilo visual do app está aqui.
# Seguimos o mesmo padrão de cores do seu CSS original:
# --color-primary: #00eeff (ciano)
# --color-accent: #2567ff (azul)
# --bg-dark: #030207 (fundo escuro)
# ══════════════════════════════════════════════════════════════════════
def load_css():
    st.markdown("""
    <style>

    /* ── FONTE DO GOOGLE ──
       Importa a fonte Outfit para visual moderno e profissional */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* ── RESET GLOBAL ──
       Remove margens e paddings padrão do navegador */
    *, *::before, *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Outfit', system-ui, sans-serif;
    }

    /* ── SCROLL SUAVE ──
       Quando clicar em âncoras, o scroll é animado */
    html { scroll-behavior: smooth; }

    /* ════════════════════════════════════════════════
       OVERRIDES DO STREAMLIT
       Sobrescrevemos os estilos padrão do Streamlit
       para manter nossa identidade visual
    ════════════════════════════════════════════════ */

    /* Fundo geral do app — gradiente escuro do CSS original */
    .stApp {
        background: linear-gradient(135deg, #030207, #0a0a0f) !important;
        color: #ffffff !important;
    }

    /* Remove padding excessivo do container principal do Streamlit */
    .block-container {
        padding: 1.5rem 2rem 3rem !important;
        max-width: 100% !important;
    }

    /* Oculta elementos padrão do Streamlit que não queremos exibir */
    #MainMenu, footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }

    /* ════════════════════════════════════════════════
       SIDEBAR - PAINEL LATERAL ESQUERDO
       Estilizamos a sidebar com o tema dark do projeto
    ════════════════════════════════════════════════ */

    /* Fundo e borda da sidebar */
    section[data-testid="stSidebar"] {
        background: #0a0a0f !important;
        border-right: 1px solid rgba(0,238,255,0.15) !important;
    }

    /* Garante que todo texto dentro da sidebar seja branco */
    section[data-testid="stSidebar"] * { color: #ffffff !important; }

    /* Estiliza os expanders dentro da sidebar */
    section[data-testid="stSidebar"] .stExpander {
        border: 1px solid rgba(0,238,255,0.2) !important;
        border-radius: 0.6rem !important;
        background: rgba(0,238,255,0.03) !important;
    }

    /* ════════════════════════════════════════════════
       BOTÃO DE FECHAR/ABRIR A SIDEBAR
       Este é o botão ">" que aparece na borda da sidebar.
       Estilizamos para combinar com o tema do projeto.
    ════════════════════════════════════════════════ */

    /* Botão quando a sidebar está FECHADA (fica visível na borda esquerda) */
    button[data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        background: rgba(0,238,255,0.08) !important;
        border: 1px solid rgba(0,238,255,0.3) !important;
        border-radius: 0 0.6rem 0.6rem 0 !important;
        color: #00eeff !important;
        width: 1.8rem !important;
        height: 3rem !important;
        transition: all 0.3s ease !important;
        top: 50% !important;
    }

    /* Efeito hover no botão de toggle da sidebar */
    button[data-testid="collapsedControl"]:hover {
        background: rgba(0,238,255,0.2) !important;
        box-shadow: 0 0 12px rgba(0,238,255,0.3) !important;
        border-color: #00eeff !important;
    }

    /* ════════════════════════════════════════════════
       SCROLLBAR PERSONALIZADA
       Igual ao ::-webkit-scrollbar do CSS original
    ════════════════════════════════════════════════ */

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #030207; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00eeff, #2567ff);
        border-radius: 4px;
    }

    /* ════════════════════════════════════════════════
       HERO SECTION - Faixa com a citação motivacional
       Equivalente ao .hero do styleprincipalcomentado.css
    ════════════════════════════════════════════════ */

    .hero {
        background: linear-gradient(rgba(0,0,0,0.1), #030207);
        min-height: 32vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 3rem 2rem 2rem;
        position: relative;
        overflow: hidden;
        border-radius: 1rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(0,238,255,0.08);
    }

    /* Overlay translúcido sobre a hero (igual ao .hero::before do CSS original) */
    .hero::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(135deg,
            rgba(0,238,255,0.03),
            rgba(37,103,255,0.03));
        pointer-events: none;
    }

    /* Texto da citação principal — com borda esquerda neon */
    .hero-quote {
        font-size: clamp(1rem, 2.5vw, 1.4rem);
        font-weight: 300;
        color: rgba(255,255,255,0.85);
        font-style: italic;
        max-width: 680px;
        margin: 0 auto 0.4rem;
        line-height: 1.7;
        border-left: 3px solid #00eeff;
        padding-left: 1.5rem;
        text-align: left;
    }

    /* Subtítulo da citação — mais apagado que o principal */
    .hero-quote-sub {
        font-size: clamp(0.82rem, 2vw, 0.98rem);
        color: rgba(255,255,255,0.45);
        font-style: italic;
        max-width: 680px;
        margin: 0 auto;
        text-align: left;
        padding-left: 1.5rem;
    }

    /* ════════════════════════════════════════════════
       TÍTULO PRINCIPAL
       Equivalente ao .home-content h1 do CSS original
    ════════════════════════════════════════════════ */

    .main-title {
        font-size: clamp(1.8rem, 4vw, 2.8rem);
        font-weight: 300;
        background: linear-gradient(135deg, #00eeff, #2567ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.4rem;
        line-height: 1.2;
    }

    /* Subtítulo com as especialidades */
    .main-subtitle {
        font-size: clamp(0.78rem, 1.6vw, 0.9rem);
        color: rgba(255,255,255,0.55);
        line-height: 1.6;
        margin-bottom: 2rem;
    }

    /* ════════════════════════════════════════════════
       DIVISOR NEON
       Linha horizontal com gradiente ciano para separar seções
    ════════════════════════════════════════════════ */

    .neon-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #00eeff, transparent);
        border: none;
        opacity: 0.25;
        margin: 2rem 0;
    }

    /* ════════════════════════════════════════════════
       TÍTULOS DAS SEÇÕES
       Equivalente ao .section__title do CSS original
    ════════════════════════════════════════════════ */

    .section-title {
        font-size: clamp(1.3rem, 3vw, 1.9rem);
        font-weight: 300;
        background: linear-gradient(135deg, #00eeff, #2567ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid rgba(0,238,255,0.2);
    }

    /* ════════════════════════════════════════════════
       SEÇÃO SOBRE MIM
    ════════════════════════════════════════════════ */

    /* Texto da seção Sobre — justificado para aparência profissional */
    .sobre-texto {
        font-size: 0.93rem;
        line-height: 1.9;
        color: rgba(255,255,255,0.82);
        text-align: justify;
    }
    .sobre-texto p { margin-bottom: 1rem; }
    .sobre-texto p:last-child { margin-bottom: 0; }

    /* Container da foto circular */
    .sobre-foto {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 0.5rem;
    }

    /* Foto circular com borda e brilho neon
       Igual ao efeito das imagens no CSS original */
    .sobre-foto img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00eeff;
        box-shadow: 0 0 28px rgba(0,238,255,0.45);
        transition: all 0.5s ease;
    }

    /* Efeito hover na foto — zoom e brilho mais intenso */
    .sobre-foto img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 45px rgba(0,238,255,0.65);
    }

    /* ════════════════════════════════════════════════
       CARDS DE HABILIDADES (SKILLS)
       Fundo dark com borda superior neon
    ════════════════════════════════════════════════ */

    .skill-card {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 1rem;
        border: 1px solid rgba(255,255,255,0.07);
        border-top: 3px solid #00eeff;
        padding: 1.5rem;
        height: 100%;
        transition: all 0.3s ease;
    }

    /* Hover nos cards de skill — sobe e brilha */
    .skill-card:hover {
        background: rgba(255,255,255,0.08) !important;
        box-shadow: 0 0 22px rgba(0,238,255,0.15);
        transform: translateY(-5px);
    }

    /* Título de cada categoria de skill */
    .skill-card h3 {
        color: #00eeff !important;
        font-size: 0.95rem;
        margin-bottom: 1rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Lista de habilidades sem marcadores padrão */
    .skill-card ul { list-style: none; padding: 0; }

    /* Cada item da lista com marcador customizado */
    .skill-card li {
        position: relative;
        padding-left: 1.2rem;
        margin-bottom: 0.5rem;
        font-size: 0.87rem;
        color: rgba(255,255,255,0.78) !important;
        line-height: 1.5;
    }

    /* Marcador "✓" verde antes de cada item */
    .skill-card li::before {
        content: '✓';
        color: #00FF41;
        font-weight: bold;
        position: absolute;
        left: 0;
    }

    /* ════════════════════════════════════════════════
       CARDS DO PORTFÓLIO
    ════════════════════════════════════════════════ */

    /* Container do card */
    .portifolio-box {
        position: relative;
        border-radius: 0.8rem;
        box-shadow: 0 0 0.6rem rgba(20,116,180,0.4);
        overflow: hidden;
        background: #1a1a2e !important;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }

    /* Hover no card — sobe e intensifica o brilho */
    .portifolio-box:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 28px rgba(0,238,255,0.4);
    }

    /* Imagem do projeto */
    .portifolio-box img {
        width: 100%;
        height: 185px;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }

    /* Zoom na imagem ao passar o mouse */
    .portifolio-box:hover img { transform: scale(1.08); }

    /* Overlay que sobe ao passar o mouse */
    .portifolio-layer {
        position: absolute;
        bottom: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(transparent, rgba(0,238,255,0.93));
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        text-align: center;
        padding: 1.2rem;
        opacity: 0;
        transition: opacity 0.4s ease;
    }

    /* Torna o overlay visível no hover */
    .portifolio-box:hover .portifolio-layer { opacity: 1; }

    /* Título do projeto no overlay */
    .portifolio-layer h4 {
        color: #030207 !important;
        font-size: 0.95rem;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
        font-weight: 600;
    }

    /* Descrição do projeto */
    .portifolio-layer p {
        color: #030207 !important;
        font-size: 0.78rem;
        margin-bottom: 0.3rem;
    }

    /* Badge da tecnologia usada */
    .tec-badge {
        font-size: 0.68rem;
        background: rgba(3,2,7,0.25);
        color: #030207 !important;
        padding: 0.15rem 0.6rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
        display: inline-block;
    }

    /* Botão de link do projeto — círculo com seta */
    .portifolio-layer a {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 2.2rem;
        height: 2.2rem;
        background: #ffffff;
        border-radius: 50%;
        color: #030207 !important;
        font-size: 1rem;
        text-decoration: none;
        transition: all 0.3s ease;
        margin-top: 0.3rem;
    }

    /* Hover no botão do projeto */
    .portifolio-layer a:hover {
        background: #030207;
        color: #00eeff !important;
    }

    /* ════════════════════════════════════════════════
       CARDS DE EXPERIÊNCIA PROFISSIONAL
       Equivalente ao .experience-item do stylecurr.css
       com borda esquerda neon e efeito slide no hover
    ════════════════════════════════════════════════ */

    .exp-card {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 1rem;
        border-left: 4px solid #00eeff;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }

    /* Hover — desliza para direita e brilha */
    .exp-card:hover {
        background: rgba(255,255,255,0.07) !important;
        box-shadow: 0 0 22px rgba(0,238,255,0.13);
        transform: translateX(5px);
    }

    /* Cabeçalho do card (ícone + título + empresa) */
    .exp-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.4rem;
    }

    .exp-icon { font-size: 1.6rem; }

    /* Cargo/título do trabalho */
    .exp-card .job-title {
        font-size: 1.08rem;
        font-weight: 600;
        color: #ffffff !important;
        margin-bottom: 0;
    }

    /* Nome da empresa em ciano (cor de destaque) */
    .exp-card .company {
        font-size: 0.92rem;
        color: #00eeff !important;
        margin-bottom: 0.2rem;
        font-weight: 500;
    }

    /* Período em itálico e apagado */
    .exp-card .period {
        font-size: 0.78rem;
        color: rgba(255,255,255,0.42) !important;
        font-style: italic;
        margin-bottom: 1rem;
    }

    /* Subtítulos internos (Resultados / Atividades) */
    .exp-sublabel {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.5) !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin: 0.8rem 0 0.4rem;
        font-weight: 500;
    }

    /* Lista de itens (resultados e atividades) */
    .exp-list { list-style: none; padding: 0; margin: 0; }
    .exp-list li {
        position: relative;
        padding-left: 1.2rem;
        margin-bottom: 0.35rem;
        font-size: 0.87rem;
        color: rgba(255,255,255,0.72) !important;
        line-height: 1.55;
    }

    /* Marcador "•" ciano para atividades */
    .exp-list li::before {
        content: '•';
        color: #00eeff;
        font-weight: bold;
        position: absolute;
        left: 0;
    }

    /* Marcador "✦" verde para resultados (diferencia visualmente) */
    .exp-list.resultados li::before {
        content: '✦';
        color: #00FF41;
        font-size: 0.7rem;
        top: 0.1rem;
    }

    /* ════════════════════════════════════════════════
       CARDS DE FORMAÇÃO ACADÊMICA
       Mesmo layout dos cards de experiência, mas com
       borda azul (#2567ff) para diferenciar visualmente
    ════════════════════════════════════════════════ */

    .edu-card {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 1rem;
        border-left: 4px solid #2567ff;
        padding: 1.2rem 1.8rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
    }

    /* Hover — mesmo efeito de deslize dos cards de experiência */
    .edu-card:hover {
        background: rgba(255,255,255,0.07) !important;
        box-shadow: 0 0 18px rgba(37,103,255,0.2);
        transform: translateX(5px);
    }

    /* Ícone da formação */
    .edu-icon { font-size: 2rem; min-width: 2.5rem; text-align: center; }

    /* Área de informações do curso */
    .edu-info { flex: 1; }

    /* Nome do curso */
    .edu-curso {
        font-size: 1rem;
        font-weight: 600;
        color: #ffffff !important;
        margin-bottom: 0.2rem;
    }

    /* Nome da instituição em azul */
    .edu-inst {
        font-size: 0.88rem;
        color: #2567ff !important;
        font-weight: 500;
        margin-bottom: 0.2rem;
    }

    /* Período em itálico e apagado */
    .edu-periodo {
        font-size: 0.76rem;
        color: rgba(255,255,255,0.42) !important;
        font-style: italic;
    }

    /* Badge "Em andamento" — borda e texto ciano */
    .edu-badge-andamento {
        font-size: 0.68rem;
        background: rgba(0,238,255,0.12);
        color: #00eeff !important;
        border: 1px solid rgba(0,238,255,0.3);
        padding: 0.2rem 0.7rem;
        border-radius: 1rem;
        white-space: nowrap;
    }

    /* Badge "Concluído" — borda e texto verde */
    .edu-badge-concluido {
        font-size: 0.68rem;
        background: rgba(0,255,65,0.1);
        color: #00FF41 !important;
        border: 1px solid rgba(0,255,65,0.3);
        padding: 0.2rem 0.7rem;
        border-radius: 1rem;
        white-space: nowrap;
    }

    /* ════════════════════════════════════════════════
       SEÇÃO DE CONTATO NA SIDEBAR
    ════════════════════════════════════════════════ */

    .contato-wrapper {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
        padding: 0.25rem 0;
    }

    .contato-item {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.55rem 0.8rem;
        background: rgba(0,238,255,0.04);
        border-radius: 0.6rem;
        border-left: 3px solid #00eeff;
        text-decoration: none !important;
        transition: all 0.3s ease;
        width: 100%;
        box-sizing: border-box;
    }

    .contato-item:hover {
        background: rgba(0,238,255,0.1);
        box-shadow: 0 0 10px rgba(0,238,255,0.18);
        transform: translateX(3px);
    }

    .contato-label {
        font-size: 0.62rem !important;
        color: rgba(255,255,255,0.38) !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 0.05rem;
        display: block;
    }

    .contato-valor {
        font-size: 0.8rem !important;
        color: #ffffff !important;
        font-weight: 500;
        display: block;
        word-break: break-all;
    }

    .contato-valor.link { 
        color: #00eeff !important;
        word-break: break-all;
    }

    /* ── ÍCONES DAS REDES SOCIAIS ── */
    .social-midia {
        display: flex;
        justify-content: center;
        gap: 0.55rem;
        margin-top: 0.9rem;
        flex-wrap: wrap;
    }

    .social-midia a {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 2.4rem;
        height: 2.5rem;
        background: transparent;
        border: 0.10rem solid #00eeff;
        border-radius: 50%;
        color: #00eeff !important;
        text-decoration: none !important;
        transition: all 0.3s ease;
        padding: 0.5rem;
    }

    .social-midia a:hover {
        background-color: #00eeff;
        box-shadow: 0 0 0.5rem #00eeff;
        transform: scale(1.12);
    }

    .social-midia a img {
        width: 1.1rem;
        height: 1.1rem;
        filter: invert(1) sepia(1) saturate(5) hue-rotate(160deg);
        transition: all 0.3s ease;
    }

    .social-midia a:hover img { filter: brightness(0); }

    /* ════════════════════════════════════════════════
       FOOTER - RODAPÉ
    ════════════════════════════════════════════════ */

    .footer {
        background: #0a0a0f;
        border-top: 1px solid rgba(255,255,255,0.07);
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
        border-radius: 1rem;
    }
    .footer p { color: rgba(255,255,255,0.45) !important; font-size: 0.85rem; }
    
    </style>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: ÍCONES DE REDES SOCIAIS
# Usa imagens SVG do simpleicons.org para ter os ícones corretos
# (LinkedIn, GitHub, YouTube, Outlook)
# ══════════════════════════════════════════════════════════════════════
def social_links():
    st.markdown(
        '<div class="social-midia">'

        # LinkedIn — ícone oficial azul
        '<a href="https://www.linkedin.com/in/rafael-silva-160274b0/" '
        'target="_blank" title="LinkedIn">'
        '<img src="https://cdn.simpleicons.org/linkedin" alt="LinkedIn"/>'
        '</a>'

        # GitHub — ícone oficial preto
        '<a href="https://github.com/rafa10bjj" '
        'target="_blank" title="GitHub">'
        '<img src="https://cdn.simpleicons.org/github" alt="GitHub"/>'
        '</a>'

        # YouTube — ícone oficial vermelho
        '<a href="https://www.youtube.com/@rafaelrafa10bjj" '
        'target="_blank" title="YouTube">'
        '<img src="https://cdn.simpleicons.org/youtube" alt="YouTube"/>'
        '</a>'

        # Email via Outlook
        '<a href="mailto:rafa10kl@hotmail.com" title="E-mail">'
        '<img src="https://cdn.simpleicons.org/microsoftoutlook" alt="E-mail"/>'
        '</a>'

        '</div>',
        unsafe_allow_html=True
    )


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: SEÇÃO DE CONTATO DA SIDEBAR
# Exibe cards com ícone, label e valor para cada informação de contato
# ══════════════════════════════════════════════════════════════════════
def show_contato():
    st.markdown(
        '<div class="contato-wrapper">'

        # Localização — apenas div (não é link)
        '<div class="contato-item">'
        '<span style="font-size:1rem;">📍</span>'
        '<div>'
        '<span class="contato-label">Localização</span>'
        '<span class="contato-valor">Recife, Pernambuco</span>'
        '</div>'
        '</div>'

        # Telefone — apenas div (não é link)
        '<div class="contato-item">'
        '<span style="font-size:1rem;">📱</span>'
        '<div>'
        '<span class="contato-label">Telefone</span>'
        '<span class="contato-valor">(81) 99504-6827</span>'
        '</div>'
        '</div>'

        # Email — é um link clicável (abre o cliente de e-mail)
        '<a href="mailto:rafa10kl@hotmail.com" class="contato-item">'
        '<span style="font-size:1rem;">✉️</span>'
        '<div>'
        '<span class="contato-label">E-mail</span>'
        '<span class="contato-valor link">rafa10kl@hotmail.com</span>'
        '</div>'
        '</a>'

        # LinkedIn — é um link clicável (abre nova aba)
        '<a href="https://www.linkedin.com/in/rafael-silva-160274b0/" '
        'target="_blank" class="contato-item">'
        '<span style="font-size:1rem;">💼</span>'
        '<div>'
        '<span class="contato-label">LinkedIn</span>'
        '<span class="contato-valor link">rafael-silva-160274b0</span>'
        '</div>'
        '</a>'

        # GitHub — é um link clicável (abre nova aba)
        '<a href="https://github.com/rafa10bjj" '
        'target="_blank" class="contato-item">'
        '<span style="font-size:1rem;">🐙</span>'
        '<div>'
        '<span class="contato-label">GitHub</span>'
        '<span class="contato-valor link">rafa10bjj</span>'
        '</div>'
        '</a>'

        '</div>',
        unsafe_allow_html=True
    )
    # Renderiza os ícones sociais abaixo dos cards de contato
    social_links()


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: SEÇÃO DE HABILIDADES
# Renderiza 3 colunas com os cards de skills definidos em SKILLS
# ══════════════════════════════════════════════════════════════════════
def show_skills():
    st.markdown('<p class="section-title">🛠️ Habilidades Técnicas</p>', unsafe_allow_html=True)

    # Verifica se há habilidades para exibir
    if not SKILLS:
        st.warning("Nenhuma habilidade cadastrada.")
        return

    # Cria 3 colunas de tamanho igual
    cols = st.columns(3)

    # Para cada categoria de skill, pega a coluna correspondente pelo índice
    for idx, (titulo, itens) in enumerate(SKILLS.items()):
        if idx >= len(cols):
            st.warning(f"Número de categorias de habilidades excede o número de colunas. Categoria '{titulo}' não será exibida.")
            continue
        with cols[idx]:
            # Gera os <li> de cada habilidade
            items_html = "".join(f"<li>{item}</li>" for item in itens)
            st.markdown(
                f'<div class="skill-card">'
                f'<h3>{titulo}</h3>'
                f'<ul>{items_html}</ul>'
                f'</div>',
                unsafe_allow_html=True
            )


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: SEÇÃO DE EXPERIÊNCIA PROFISSIONAL
# Renderiza cards com ícone, título, empresa, período e listas
# de resultados e atividades
# ══════════════════════════════════════════════════════════════════════
def show_experience():
    st.markdown(
        '<p class="section-title">💼 Experiência Profissional</p>',
        unsafe_allow_html=True
    )

    # Verifica se há experiências para exibir
    if not EXPERIENCE:
        st.warning("Nenhuma experiência profissional cadastrada.")
        return

    for exp in EXPERIENCE:
        # Verifica se as chaves obrigatórias estão presentes
        if not all(key in exp for key in ["titulo", "empresa", "periodo", "icon", "resultados", "atividades"]):
            st.error("Erro nos dados de experiência: chaves obrigatórias ausentes.")
            continue

        # Gera os <li> de resultados e atividades separadamente
        res_html = "".join(f"<li>{r}</li>" for r in exp["resultados"])
        atv_html = "".join(f"<li>{a}</li>" for a in exp["atividades"])

        st.markdown(
            f'<div class="exp-card">'

            # Cabeçalho: ícone + cargo + empresa
            f'<div class="exp-header">'
            f'<span class="exp-icon">{exp["icon"]}</span>'
            f'<div>'
            f'<p class="job-title">{exp["titulo"]}</p>'
            f'<p class="company">{exp["empresa"]}</p>'
            f'</div>'
            f'</div>'

            # Período
            f'<p class="period">📅 {exp["periodo"]}</p>'

            # Lista de resultados com marcador verde "✦"
            f'<p class="exp-sublabel">✦ Resultados</p>'
            f'<ul class="exp-list resultados">{res_html}</ul>'

            # Lista de atividades com marcador ciano "•"
            f'<p class="exp-sublabel">• Atividades</p>'
            f'<ul class="exp-list">{atv_html}</ul>'

            f'</div>',
            unsafe_allow_html=True
        )


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: SEÇÃO DE FORMAÇÃO ACADÊMICA
# Mesmo layout dos cards de experiência com badge de status
# ══════════════════════════════════════════════════════════════════════
def show_education():
    st.markdown(
        '<p class="section-title">🎓 Formação Acadêmica</p>',
        unsafe_allow_html=True
    )

    # Verifica se há formação acadêmica para exibir
    if not EDUCATION:
        st.warning("Nenhuma formação acadêmica cadastrada.")
        return

    for edu in EDUCATION:
        # Verifica se as chaves obrigatórias estão presentes
        if not all(key in edu for key in ["curso", "instituicao", "periodo", "icon", "status"]):
            st.error("Erro nos dados de formação acadêmica: chaves obrigatórias ausentes.")
            continue

        # Define o badge correto baseado no status
        if edu["status"] == "andamento":
            badge = '<span class="edu-badge-andamento">⏳ Em andamento</span>'
        elif edu["status"] == "concluido":
            badge = '<span class="edu-badge-concluido">✓ Concluído</span>'
        else:
            st.warning(f"Status desconhecido para formação: {edu['status']}")
            badge = '<span class="edu-badge-andamento">⏳ Em andamento</span>'

        st.markdown(
            f'<div class="edu-card">'
            f'<span class="edu-icon">{edu["icon"]}</span>'  # Ícone emoji
            f'<div class="edu-info">'
            f'<p class="edu-curso">{edu["curso"]}</p>'          # Nome do curso
            f'<p class="edu-inst">{edu["instituicao"]}</p>'     # Instituição
            f'<p class="edu-periodo">📅 {edu["periodo"]}</p>'   # Período
            f'</div>'
            f'{badge}'   # Badge de status (andamento ou concluído)
            f'</div>',
            unsafe_allow_html=True
        )


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL - MAIN
# Aqui montamos toda a estrutura da página:
# 1. Sidebar (painel lateral)
# 2. Hero (faixa com citação)
# 3. Título principal
# 4. Seção Sobre Mim
# 5. Habilidades
# 6. Experiência
# 7. Formação
# 8. Footer
# ══════════════════════════════════════════════════════════════════════
def main():
    load_css()

    # ── 1. SIDEBAR ────────────────────────────────────────────────────
    with st.sidebar:

        # Foto de perfil circular com borda neon ciano
        st.markdown(
            f'<div style="text-align:center;padding:1.5rem 0 1rem;">'
            f'<img src="{foto_perfil}" style="'
            f'width:155px;'
            f'height:155px;'
            f'border-radius:50%;'        # Torna a foto circular
            f'object-fit:cover;'         # Preenche sem distorcer
            f'border:3px solid #00eeff;' # Borda neon ciano
            f'box-shadow:0 0 25px rgba(0,238,255,0.4);' # Brilho externo
            f'margin-bottom:0.75rem;"/>'
            # Nome com letras maiúsculas e peso leve
            f'<h2 style="color:#ffffff;font-weight:300;font-size:1.05rem;'
            f'margin-bottom:0.3rem;text-transform:uppercase;letter-spacing:0.05em;">'
            f'Rafael Rodrigues</h2>'
            # Subtítulo em ciano com as especialidades
            f'<p style="color:#00eeff;font-size:0.75rem;line-height:1.5;">'
            f'Analista de Dados | Logística | Supply Chain</p>'
            f'</div>',
            unsafe_allow_html=True
        )

        # Expander de Contato — começa aberto (expanded=True)
        with st.expander("📬 Contato", expanded=True):
            show_contato()

        st.divider()    

        st.sidebar.markdown("Desenvolvido por : [Rafa10](https://www.linkedin.com/in/rafael-silva-160274b0)", text_alignment='center')

    # ── 2. HERO ───────────────────────────────────────────────────────
    # Faixa com as citações motivacionais
    st.markdown(
        '<section class="hero">'
        '<p class="hero-quote">'
        '"Em tudo na vida, você não precisa ser bom para começar.<br>'
        'Você tem que se permitir começar para ser bom."'
        '</p>'
        '<p class="hero-quote-sub">'
        '"Talento pode ser herdado, mas o esforço é escolhido."'
        '</p>'
        '</section>',
        unsafe_allow_html=True
    )

    # ── 3. TÍTULO PRINCIPAL ───────────────────────────────────────────
    st.markdown(
        '<h1 class="main-title">Rafael Rodrigues</h1>'
        '<p class="main-subtitle">'
        'Analista de Dados · Power BI · SQL Server · Python · Excel · '
        'Logística · Supply Chain · Gestão de Estoque · Liderança'
        '</p>',
        unsafe_allow_html=True
    )

    # ── 4. SOBRE MIM ──────────────────────────────────────────────────
    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-title">👨‍💻 Sobre Mim</p>',
        unsafe_allow_html=True
    )

    # Duas colunas: texto (3 partes) + foto (1 parte)
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            '<div class="sobre-texto">'
            '<p>Profissional com mais de 20 anos de sólida trajetória em Logística e Supply Chain, unindo '
            'essa profunda visão de negócio à Análise de Dados. Formado na área e com MBA em Logística '
            'Empresarial, sempre tive grande atração por tecnologia e programação.</p>'
            '<p>Ao vivenciar diariamente os desafios operacionais do setor, percebi que a chave para '
            'otimizar processos, reduzir custos e mitigar perdas está nas decisões orientadas a dados. Isso me motivou a me '
            'especializar em Excel, VBA, Power BI, SQL e, mais recentemente, Python para Análise de Dados.</p>'
            '<p>Hoje, combino minhas duas décadas de visão prática com uma sólida capacidade técnica em dados, uma combinação '
            'que me permite não apenas gerar relatórios, mas entender o impacto real das métricas no negócio. Este '
            'portfólio foi criado por mim como reflexo desse aprendizado contínuo e dedicação.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f'<div class="sobre-foto">'
            f'<img src="{foto_sobre}" alt="Rafael Rodrigues"/>'
            f'</div>',
            unsafe_allow_html=True
        )

    # ── 5. HABILIDADES ────────────────────────────────────────────────
    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    show_skills()

    # ── 6. EXPERIÊNCIA PROFISSIONAL ───────────────────────────────────
    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    show_experience()

    # ── 7. FORMAÇÃO ACADÊMICA ─────────────────────────────────────────
    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    show_education()

    # ── 8. FOOTER ─────────────────────────────────────────────────────
    st.markdown(
        '<div class="footer">'
        '<p>Desenvolvido por '
        '<strong style="color:#00eeff;">Rafael Rodrigues</strong>'
        '</p>'
        '<p style="margin-top:0.3rem;">'
        '📧 rafa10kl@hotmail.com &nbsp;·&nbsp; 📍 Recife, PE'
        '</p>'
        '</div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════════════════════════
# PONTO DE ENTRADA DO PROGRAMA
# ══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    main()