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
        return ""  # Retorna string vazia se o arquivo não existir (evita crash)

# ══════════════════════════════════════════════════════════════════════
# PRÉ-CARREGAMENTO DAS IMAGENS
# Carregamos todas as imagens em base64 no início para não repetir
# a função a cada renderização da página
# ══════════════════════════════════════════════════════════════════════
foto_perfil = get_img_base64("img/img01.png")   # Foto do perfil da sidebar
foto_sobre  = get_img_base64("img/img02.png")   # Foto da seção Sobre Mim

# --- PROJETOS DO PORTFÓLIO ---
# Lista de dicionários, cada um representando um projeto
PROJECTS = [
     {
        "titulo": "Performance de Vendas",
        "desc":   "Análise de performance comercial",
        "tec":    "Power BI",
        "img":    get_img_base64("img/img03.png"),
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiYzIxNGU1ZmQtNTIwZC00YTQ0LTliNGItZTRhZTExMjlkOGNjIiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
    {
        "titulo": "Infográfico de Vendas",
        "desc":   "Dashboard interativo de vendas",
        "tec":    "Power BI",
        "img":    get_img_base64("img/infografico.png"),  # Imagem em base64
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiN2RkZjI3YjItZDE1NS00ZjNlLWJjMTAtZWE2YjA1N2VhZDNlIiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
   
    {
        "titulo": "HPN Reavy Power Nutrition",
        "desc":   "Dashboard nutricional e esportivo",
        "tec":    "Power BI",
        "img":    get_img_base64("img/HPN.png"),
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiZGMzYTQ0MzktOGYyOS00YWU4LTlkMDYtYTUyYmNjZmFlZmZmIiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
    {
        "titulo": "Análise da Lista de Espera para Transplante de Rins no Brasil (2000-2017)",
        "desc":   "Fila de espera",
        "tec":    "Power BI",
        "img":    get_img_base64("img/img04.png"),
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiNzQyZDVjMzgtODNiYy00M2VkLTgyNWQtYjc4NmI3ZGM1OTQxIiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
    {
        "titulo": "Análise ENEM 2019",
        "desc":   "Análise de dados educacionais",
        "tec":    "Power BI",
        "img":    get_img_base64("img/Enem2019-01.png"),
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiNDEyNjllYjMtMDI4Ni00OGFkLWE2NTgtZTAzZTJmMzE4YzkzIiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
    {
        "titulo": "Análise Comercial",
        "desc":   "Análise de dados de vendas",
        "tec":    "Power BI",
        "img":    get_img_base64("img/img05.png"),
        "link":   "https://app.powerbi.com/view?r=eyJrIjoiODhkYTY1ODAtM2QzYy00YzNmLTkxYTAtNjdiMmE1NWJmYzk3IiwidCI6ImY1MDM4NzBkLTBhYWUtNDI1Mi05ZjE1LWQ2MTg5NmY5ZjZmZiJ9"
    },
    {
        "titulo": "Engajamento Instagram",
        "desc":   "Análise de métricas de redes sociais",
        "tec":    "Python",
        "img":    get_img_base64("img/06.jpg"),
        "link":   "https://github.com/rafa10bjj/Engajamento-Instagram"
    },
    {
        "titulo": "Análise Lojas Seu João",
        "desc":   "Análise de dados de varejo",
        "tec":    "Python",
        "img":    get_img_base64("img/rafael.onefre_a_computer_screen_showing_a_steady_increasing_g_a36c4cf4-d8b4-456f-8cd7-82c0944c7359_1.png"),
        "link":   "https://github.com/rafa10bjj/Desafio_Alura_Store"
    },
    {
        "titulo": "x-Telecom",
        "desc":   "Análise de churn em telecomunicações",
        "tec":    "Python",
        "img":    get_img_base64("img/Captura de tela 2025-06-10 171548.png"),
        "link":   "https://github.com/rafa10bjj/Telecom-X"
    },
    {
        "titulo": "Análise de Dados Python",
        "desc":   "Scripts e análises diversas",
        "tec":    "Python",
        "img":    get_img_base64("img/06.jpg"),
        "link":   "https://github.com/rafa10bjj/Python_an-lise_de_dados"
    },
        {
        "titulo": "🚀 Previsão de Inadimplência com SQL + Python",
        "desc":   "Scripts e análises diversas",
        "tec":    "Python",
        "img":    get_img_base64("img/img06.png"),
        "link":   "https://github.com/rafa10bjj/PROJETO-PARA-PREVER-INADIMPLENCIA/tree/main"
    },
]

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

    /* ── SCROLL SUAVE ── */
    html { scroll-behavior: smooth; }

    /* ════════════════════════════════════════════════
       OVERRIDES DO STREAMLIT
    ════════════════════════════════════════════════ */

    /* Fundo geral do app — gradiente escuro */
    .stApp {
        background: linear-gradient(135deg, #030207, #0a0a0f) !important;
        color: #ffffff !important;
    }

    /* Remove padding excessivo do container principal do Streamlit */
    .block-container {
        padding: 1.5rem 2rem 3rem !important;
        max-width: 100% !important;
    }

    /* Oculta elementos padrão do Streamlit */
    #MainMenu, footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }

    /* ════════════════════════════════════════════════
       SIDEBAR - PAINEL LATERAL ESQUERDO
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
    ════════════════════════════════════════════════ */

    /* Botão quando a sidebar está FECHADA */
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

    button[data-testid="collapsedControl"]:hover {
        background: rgba(0,238,255,0.2) !important;
        box-shadow: 0 0 12px rgba(0,238,255,0.3) !important;
        border-color: #00eeff !important;
    }

    /* ════════════════════════════════════════════════
       SCROLLBAR PERSONALIZADA
    ════════════════════════════════════════════════ */

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #030207; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00eeff, #2567ff);
        border-radius: 4px;
    }

    /* ════════════════════════════════════════════════
       HERO SECTION
    ════════════════════════════════════════════════ */

    .hero {
        background: linear-gradient(rgba(0,0,0,0.1), #030207);
        min-height: 30vh;
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
       DIVISOR NEON
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
       CARDS DO PORTFÓLIO
    ════════════════════════════════════════════════ */

    .portifolio-box {
        position: relative;
        border-radius: 0.8rem;
        box-shadow: 0 0 0.6rem rgba(20,116,180,0.4);
        overflow: hidden;
        background: #1a1a2e !important;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-bottom: 1.2rem;
    }

    .portifolio-box:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 28px rgba(0,238,255,0.45);
    }

    .portifolio-box img {
        width: 100%;
        height: 185px;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }

    .portifolio-box:hover img { transform: scale(1.08); }

    .portifolio-placeholder {
        width: 100%;
        height: 185px;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: transform 0.5s ease;
    }
    .portifolio-box:hover .portifolio-placeholder {
        transform: scale(1.08);
    }

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

    .portifolio-box:hover .portifolio-layer { opacity: 1; }

    .portifolio-layer h4 {
        color: #030207 !important;
        font-size: 0.95rem;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
        font-weight: 600;
    }

    .portifolio-layer p {
        color: #030207 !important;
        font-size: 0.78rem;
        margin-bottom: 0.3rem;
    }

    .tec-badge {
        font-size: 0.68rem;
        background: rgba(3,2,7,0.25);
        color: #030207 !important;
        padding: 0.15rem 0.6rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
        display: inline-block;
    }

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

    .portifolio-layer a:hover {
        background: #030207;
        color: #00eeff !important;
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
    }

    .contato-valor.link { color: #00eeff !important; }

    /* ════════════════════════════════════════════════
       ÍCONES DAS REDES SOCIAIS
    ════════════════════════════════════════════════ */

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
       DASHBOARD METRICS (STATS CARDS)
    ════════════════════════════════════════════════ */
    .stat-card {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 0.8rem !important;
        padding: 1rem 1.5rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(5px);
    }
    .stat-card:hover {
        background: rgba(255, 255, 255, 0.06) !important;
        border-color: rgba(0, 238, 255, 0.2) !important;
        box-shadow: 0 0 15px rgba(0, 238, 255, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    .stat-icon {
        font-size: 1.8rem !important;
    }
    .stat-info {
        display: flex !important;
        flex-direction: column !important;
    }
    .stat-value {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        line-height: 1.2 !important;
    }
    .stat-label {
        font-size: 0.75rem !important;
        color: rgba(255, 255, 255, 0.45) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }

    /* ── STREAMLIT TABS CUSTOM STYLING ── */
    div[data-baseweb="tab-list"] {
        gap: 1.5rem !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.07) !important;
        padding-bottom: 0.2rem !important;
        margin-top: 1rem !important;
    }
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: rgba(255, 255, 255, 0.5) !important;
        border: none !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00eeff !important;
        border-bottom: 2px solid #00eeff !important;
        text-shadow: 0 0 10px rgba(0, 238, 255, 0.4);
    }
    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
    }

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
# FUNÇÃO: SEÇÃO DE PORTFÓLIO
# Renderiza os projetos com dashboard de métricas, busca por texto e abas por tecnologia
# ══════════════════════════════════════════════════════════════════════
def show_projects():
    st.markdown('<p class="section-title">🚀 Portfólio de Projetos</p>', unsafe_allow_html=True)

    # ── MÉTRICAS DO PORTFÓLIO ──
    total_projs = len(PROJECTS)
    pbi_projs = len([p for p in PROJECTS if p["tec"].lower() == "power bi"])
    py_projs = len([p for p in PROJECTS if p["tec"].lower() == "python"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">📂</span>
            <div class="stat-info">
                <span class="stat-value">{total_projs}</span>
                <span class="stat-label">Total de Projetos</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon" style="color: #ffd700;">📊</span>
            <div class="stat-info">
                <span class="stat-value">{pbi_projs}</span>
                <span class="stat-label">Power BI Dashboards</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon" style="color: #39ff14;">🐍</span>
            <div class="stat-info">
                <span class="stat-value">{py_projs}</span>
                <span class="stat-label">Python & Dados</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 1.5rem;"></div>', unsafe_allow_html=True)

    # ── BARRA DE BUSCA E ABAS ──
    search_query = st.text_input(
        "Buscar por título, descrição ou tecnologia...",
        placeholder="🔍 Digite palavras-chave (ex: Enem, Vendas, Churn, Power BI...)",
        label_visibility="collapsed"
    )

    tab_todos, tab_pbi, tab_python = st.tabs(["📂 Todos os Projetos", "📊 Power BI", "🐍 Python"])

    # Filtro por busca
    filtered = PROJECTS
    if search_query:
        q = search_query.lower().strip()
        filtered = [
            p for p in PROJECTS 
            if q in p["titulo"].lower() or q in p["desc"].lower() or q in p["tec"].lower()
        ]

    # Função auxiliar para renderizar o grid
    def render_grid(projects_list):
        if not projects_list:
            st.markdown(
                '<p style="color: rgba(255,255,255,0.4); text-align: center; padding: 3rem 0;">'
                'Nenhum projeto encontrado para esta seleção.'
                '</p>',
                unsafe_allow_html=True
            )
            return

        cols = st.columns(3)
        for idx, p in enumerate(projects_list):
            with cols[idx % 3]:
                # Exibição de imagem base64 ou gradiente elegante
                if p["img"] and p["img"].strip() != "":
                    img_html = f'<img src="{p["img"]}" alt="{p["titulo"]}">'
                else:
                    if p["tec"].lower() == "power bi":
                        gradient = "linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 140, 0, 0.2))"
                        icon = "📊"
                    else:
                        gradient = "linear-gradient(135deg, rgba(0, 238, 255, 0.1), rgba(37, 103, 255, 0.2))"
                        icon = "🐍"
                    img_html = (
                        f'<div class="portifolio-placeholder" style="background: {gradient};'
                        f'border: 1px dashed rgba(0, 238, 255, 0.25);">'
                        f'<span style="font-size: 3rem; filter: drop-shadow(0 0 10px rgba(0,238,255,0.3));">{icon}</span>'
                        f'</div>'
                    )

                st.markdown(
                    f'<div class="portifolio-box">'
                    f'{img_html}'
                    f'<div class="portifolio-layer">'          # Overlay no hover
                    f'<h4>{p["titulo"]}</h4>'
                    f'<p>{p["desc"]}</p>'
                    f'<span class="tec-badge">{p["tec"]}</span>'  # Badge da tecnologia
                    f'<a href="{p["link"]}" target="_blank">→</a>'  # Seta de acesso
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

    with tab_todos:
        render_grid(filtered)

    with tab_pbi:
        pbi_filtered = [p for p in filtered if p["tec"].lower() == "power bi"]
        render_grid(pbi_filtered)

    with tab_python:
        python_filtered = [p for p in filtered if p["tec"].lower() == "python"]
        render_grid(python_filtered)


# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL - MAIN
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
            f'border-radius:50%;'
            f'object-fit:cover;'
            f'border:3px solid #00eeff;'
            f'box-shadow:0 0 25px rgba(0,238,255,0.4);'
            f'margin-bottom:0.75rem;"/>'
            f'<h2 style="color:#ffffff;font-weight:300;font-size:1.05rem;'
            f'margin-bottom:0.3rem;text-transform:uppercase;letter-spacing:0.05em;">'
            f'Rafael Rodrigues</h2>'
            f'<p style="color:#00eeff;font-size:0.75rem;line-height:1.5;">'
            f'Analista de Dados | Logística | Supply Chain</p>'
            f'</div>',
            unsafe_allow_html=True
        )

        # Expander de Contato
        with st.expander("📬 Contato", expanded=True):
            st.markdown("""
                <p><i class="fas fa-map-marker-alt"></i> Recife, Pernambuco</p>
                <p><i class="fas fa-phone"></i> (81) 99504-6827</p>
                <p><i class="fas fa-envelope"></i> rafa10kl@hotmail.com</p>
            """, unsafe_allow_html=True)
            social_links()

        st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)   
        st.sidebar.markdown("Desenvolvido por : [Rafa10](https://www.linkedin.com/in/rafael-silva-160274b0)", text_alignment='center')

    # ── 2. HERO ───────────────────────────────────────────────────────
    st.markdown(
        '<section class="hero">'
        '<p class="hero-quote">'
        '"Aqui você encontra projetos desenvolvidos com foco em Análise de Dados, logística e supply chain.<br>'
        'Utilizando Python, Pandas, Power BI e Visualização de Dados em decisões estratégicas."'
        '</p>'
        '<p class="hero-quote-sub">'
        '"Cada projeto nasce de um problema real e termina em uma decisão mais inteligente."'
        '</p>'
        '</section>',
        unsafe_allow_html=True
    )

    # ── 6. PORTFÓLIO ──────────────────────────────────────────────────
    show_projects()  # Grid de projetos com filtros e estatísticas

    # ── 9. FOOTER ─────────────────────────────────────────────────────
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