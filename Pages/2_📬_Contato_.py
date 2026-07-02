# ══════════════════════════════════════════════════════════════════════
# IMPORTAÇÕES - Bibliotecas necessárias para o funcionamento do app
# ══════════════════════════════════════════════════════════════════════
import streamlit as st  # Framework principal para criar o app web
import base64           # Para converter imagens locais em base64 (necessário no Streamlit)
import urllib.request   # Para enviar requisição HTTP nativa (sem dependências externas)
import json             # Para tratar os dados no envio do e-mail

# ══════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DA PÁGINA
# Deve ser o PRIMEIRO comando Streamlit do arquivo
# ══════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Contato - Rafael Rodrigues",     # Título que aparece na aba do navegador
    page_icon="📬",                              # Ícone da aba do navegador
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

# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: ENVIAR DADOS DO FORMULÁRIO POR E-MAIL
# Envia via POST para o FormSubmit.co em formato AJAX/JSON
# ══════════════════════════════════════════════════════════════════════
def send_email(name, email, whatsapp, servico, message):
    url = "https://formsubmit.co/ajax/rafa10kl@hotmail.com"
    payload = {
        "Nome": name,
        "Email": email,
        "WhatsApp/Telefone": whatsapp,
        "Serviço de Interesse": servico,
        "Mensagem": message,
        "_subject": f"Novo Contato Portfólio: {name} - {servico}"
    }
    
    # Tenta obter a URL de origem da requisição do Streamlit
    referer = "http://localhost:8501/"
    origin = "http://localhost:8501"
    try:
        if hasattr(st, "context") and hasattr(st.context, "headers"):
            headers = st.context.headers
            if "referer" in headers:
                referer = headers["referer"]
            elif "host" in headers:
                proto = headers.get("x-forwarded-proto", "http")
                referer = f"{proto}://{headers['host']}/"
            if referer:
                origin = referer.rstrip("/")
    except Exception:
        pass

    headers_api = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": referer,
        "Origin": origin
    }
    
    # Tentativa de usar requests se disponível
    try:
        import requests
        response = requests.post(url, json=payload, headers=headers_api, timeout=10)
        res_json = response.json()
        success_val = res_json.get("success")
        msg_val = res_json.get("message", "")
        
        if success_val in [True, "true"]:
            return True, "success"
        elif "Activation" in msg_val or "ativação" in msg_val.lower():
            return True, "activation"
        else:
            return False, msg_val
    except Exception:
        pass
        
    # Fallback usando urllib nativo do Python (garante funcionamento sem instalar bibliotecas extras)
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            url, 
            data=data, 
            headers=headers_api
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = response.read().decode('utf-8')
            res_json = json.loads(res_data)
            success_val = res_json.get("success")
            msg_val = res_json.get("message", "")
            
            if success_val in [True, "true"] or response.status == 200:
                if "Activation" in msg_val or "ativação" in msg_val.lower() or success_val in [False, "false"]:
                    return True, "activation"
                return True, "success"
            else:
                return False, msg_val
    except Exception as e:
        print(f"Erro ao enviar formulário: {e}")
        if hasattr(e, 'read'):
            try:
                error_body = e.read().decode('utf-8')
                res_json = json.loads(error_body)
                msg_val = res_json.get("message", "")
                if "Activation" in msg_val or "ativação" in msg_val.lower():
                    return True, "activation"
            except Exception:
                pass
    return False, "Erro de conexão"

# ══════════════════════════════════════════════════════════════════════
# FUNÇÃO: CARREGAR CSS
# Todo o estilo visual do app está aqui.
# Mantém a coerência visual de cores e tipografia com as outras páginas.
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

    /* Efeito hover no botão de toggle da sidebar */
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
       HERO SECTION - Faixa com citação
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
       TÍTULO PRINCIPAL
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

    .main-subtitle {
        font-size: clamp(0.78rem, 1.6vw, 0.9rem);
        color: rgba(255,255,255,0.55);
        line-height: 1.6;
        margin-bottom: 2rem;
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

    /* ÍCONES DAS REDES SOCIAIS */
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
       CARDS DE CONTATO EXCLUSIVOS DA PÁGINA
    ════════════════════════════════════════════════ */

    .contact-page-card {
        background: rgba(255, 255, 255, 0.04) !important;
        border-radius: 1rem;
        border-left: 4px solid #00eeff;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
    }
    .contact-page-card:hover {
        background: rgba(255, 255, 255, 0.07) !important;
        box-shadow: 0 0 18px rgba(0, 238, 255, 0.2);
        transform: translateX(5px);
    }
    .contact-page-card-icon {
        font-size: 1.8rem;
        min-width: 2.2rem;
        text-align: center;
    }
    .contact-page-card-info {
        flex: 1;
    }
    .contact-page-card-title {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.4) !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 0.2rem;
    }
    .contact-page-card-value {
        font-size: 0.95rem;
        font-weight: 500;
        color: #ffffff !important;
    }
    .contact-page-card-value a {
        color: #00eeff !important;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .contact-page-card-value a:hover {
        color: #ffffff !important;
        text-shadow: 0 0 8px rgba(0, 238, 255, 0.6);
    }

    /* ════════════════════════════════════════════════
       ESTILIZAÇÃO DO FORMULÁRIO STREAMLIT
    ════════════════════════════════════════════════ */

    /* Container do Form */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(0, 238, 255, 0.15) !important;
        border-radius: 1rem !important;
        padding: 2.5rem !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    }

    /* Inputs e textarea */
    div[data-testid="stForm"] input, div[data-testid="stForm"] textarea, div[data-testid="stForm"] select {
        background-color: rgba(3, 2, 7, 0.6) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0.5rem !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stForm"] input:focus, div[data-testid="stForm"] textarea:focus {
        border-color: #00eeff !important;
        box-shadow: 0 0 10px rgba(0, 238, 255, 0.25) !important;
    }

    /* Títulos dos campos do formulário */
    div[data-testid="stForm"] label {
        color: rgba(255, 255, 255, 0.85) !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
    }

    /* Botão de Enviar */
    div[data-testid="stForm"] button[type="submit"] {
        background: linear-gradient(135deg, #00eeff, #2567ff) !important;
        color: #030207 !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.60rem 2rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        width: 100% !important;
        margin-top: 1rem !important;
    }

    div[data-testid="stForm"] button[type="submit"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 15px rgba(0, 238, 255, 0.4) !important;
        color: #030207 !important;
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
# Usa imagens SVG do simpleicons.org para ter os ícones oficiais
# ══════════════════════════════════════════════════════════════════════
def social_links():
    st.markdown(
        '<div class="social-midia">'

        # LinkedIn
        '<a href="https://www.linkedin.com/in/rafael-silva-160274b0/" '
        'target="_blank" title="LinkedIn">'
        '<img src="https://cdn.simpleicons.org/linkedin" alt="LinkedIn"/>'
        '</a>'

        # GitHub
        '<a href="https://github.com/rafa10bjj" '
        'target="_blank" title="GitHub">'
        '<img src="https://cdn.simpleicons.org/github" alt="GitHub"/>'
        '</a>'

        # YouTube
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

        # Localização
        '<div class="contato-item">'
        '<span style="font-size:1rem;">📍</span>'
        '<div>'
        '<span class="contato-label">Localização</span>'
        '<span class="contato-valor">Recife, Pernambuco</span>'
        '</div>'
        '</div>'

        # Telefone
        '<div class="contato-item">'
        '<span style="font-size:1rem;">📱</span>'
        '<div>'
        '<span class="contato-label">Telefone</span>'
        '<span class="contato-valor">(81) 99504-6827</span>'
        '</div>'
        '</div>'

        # Email
        '<a href="mailto:rafa10kl@hotmail.com" class="contato-item">'
        '<span style="font-size:1rem;">✉️</span>'
        '<div>'
        '<span class="contato-label">E-mail</span>'
        '<span class="contato-valor link">rafa10kl@hotmail.com</span>'
        '</div>'
        '</a>'

        # LinkedIn
        '<a href="https://www.linkedin.com/in/rafael-silva-160274b0/" '
        'target="_blank" class="contato-item">'
        '<span style="font-size:1rem;">💼</span>'
        '<div>'
        '<span class="contato-label">LinkedIn</span>'
        '<span class="contato-valor link">rafael-silva-160274b0</span>'
        '</div>'
        '</a>'

        # GitHub
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
# FUNÇÃO PRINCIPAL - MAIN
# Aqui montamos toda a estrutura da página
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

        # Expander de Contato — começa aberto (expanded=True)
        with st.expander("📬 Contato", expanded=True):
            show_contato()

        st.divider()    

        st.sidebar.markdown("Desenvolvido por : [Rafa10](https://www.linkedin.com/in/rafael-silva-160274b0)", text_alignment='center')

    # ── 2. HERO ───────────────────────────────────────────────────────
    st.markdown(
        '<section class="hero">'
        '<p class="hero-quote">'
        '"Grandes projetos começam com uma boa conversa. Vamos nos conectar?"'
        '</p>'
        '<p class="hero-quote-sub">'
        '"Seja para uma oportunidade, consultoria ou apenas networking, sinta-se à vontade para enviar uma mensagem."'
        '</p>'
        '</section>',
        unsafe_allow_html=True
    )

    # ── 3. TÍTULO PRINCIPAL ───────────────────────────────────────────
    st.markdown(
        '<h1 class="main-title">Fale Comigo</h1>'
        '<p class="main-subtitle">'
        'Tem interesse em algum serviço ou quer conversar sobre uma oportunidade? Preencha o formulário abaixo.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)

    # ── 4. CONTEÚDO PRINCIPAL - DUAS COLUNAS ─────────────────────────
    # Coluna 1: Informações e links rápidos
    # Coluna 2: Formulário de contato
    col1, col2 = st.columns([5, 7])

    with col1:
        st.markdown('<p class="section-title">📬 Canais de Contato</p>', unsafe_allow_html=True)
        
        # Card Localização
        st.markdown(
            '<div class="contact-page-card">'
            '<div class="contact-page-card-icon">📍</div>'
            '<div class="contact-page-card-info">'
            '<div class="contact-page-card-title">Localização</div>'
            '<div class="contact-page-card-value">Recife, Pernambuco</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # Card E-mail Direto
        st.markdown(
            '<div class="contact-page-card">'
            '<div class="contact-page-card-icon">✉️</div>'
            '<div class="contact-page-card-info">'
            '<div class="contact-page-card-title">E-mail Direto</div>'
            '<div class="contact-page-card-value"><a href="mailto:rafa10kl@hotmail.com">rafa10kl@hotmail.com</a></div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # Card WhatsApp / Celular
        st.markdown(
            '<div class="contact-page-card">'
            '<div class="contact-page-card-icon">📱</div>'
            '<div class="contact-page-card-info">'
            '<div class="contact-page-card-title">WhatsApp / Telefone</div>'
            '<div class="contact-page-card-value"><a href="https://wa.me/5581995046827" target="_blank">(81) 99504-6827</a></div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # Card LinkedIn
        st.markdown(
            '<div class="contact-page-card">'
            '<div class="contact-page-card-icon">💼</div>'
            '<div class="contact-page-card-info">'
            '<div class="contact-page-card-title">LinkedIn</div>'
            '<div class="contact-page-card-value"><a href="https://www.linkedin.com/in/rafael-silva-160274b0/" target="_blank">in/rafael-silva-160274b0</a></div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown('<p class="section-title">📨 Enviar Mensagem</p>', unsafe_allow_html=True)
        
        # Formulário Streamlit
        with st.form("contact_form", clear_on_submit=True):
            nome = st.text_input("Seu Nome *", placeholder="Digite seu nome completo...")
            email = st.text_input("Seu E-mail *", placeholder="Exemplo: nome@email.com")
            whatsapp = st.text_input("WhatsApp / Celular", placeholder="Exemplo: (81) 99999-9999")
            servico = st.selectbox(
                "Serviço de Interesse",
                [
                    "📊 Dashboards & BI (Power BI / Excel)",
                    "🐍 Automação & Scripting (Python / SQL)",
                    "🚛 Logística & Supply Chain",
                    "💡 Outro Projeto / Oportunidade"
                ]
            )
            mensagem = st.text_area("Sua Mensagem *", placeholder="Escreva detalhadamente o que você precisa ou sua proposta...", height=150)
            
            submit_button = st.form_submit_button("Enviar Mensagem 🚀")

        if submit_button:
            # Validações básicas no lado do cliente
            if not nome.strip() or not email.strip() or not mensagem.strip():
                st.warning("⚠️ Por favor, preencha todos os campos obrigatórios (*).")
            elif "@" not in email or "." not in email:
                st.error("❌ Por favor, digite um e-mail válido.")
            else:
                with st.spinner("Enviando sua mensagem..."):
                    success, status_msg = send_email(nome, email, whatsapp, servico, mensagem)
                    if success:
                        if status_msg == "activation":
                            st.info("📨 **Quase lá!** Um e-mail de ativação do **FormSubmit** foi enviado para **rafa10kl@hotmail.com**. Por favor, acesse seu e-mail e clique no link de ativação para liberar o recebimento de mensagens.")
                            st.warning("⚠️ O formulário só funcionará após clicar no link de ativação enviado para seu e-mail.")
                        else:
                            st.success("✅ Mensagem enviada com sucesso! Em breve entrarei em contato.")
                    else:
                        st.error(f"❌ Ocorreu um erro no envio ({status_msg}). Se preferir, mande diretamente para: rafa10kl@hotmail.com")

    # ── 5. FOOTER ─────────────────────────────────────────────────────
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

if __name__ == "__main__":
    main()
