"""
EduDataBR — Painel Analítico & Preditivo ENEM 2023
Aplicação Web Interativa com Acessibilidade, Tema Claro/Escuro e Paleta Azul Pastel & Bege.

Autor: Gustavo Saraiva
Repositório: https://github.com/saraivagustavo/EduDataBR
"""

import os
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="EduDataBR — Painel ENEM 2023",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. GERENCIAMENTO DE TEMA (CLARO / ESCURO) E PALETA DE CORES ACESSÍVEL
# ==============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Toggle de tema na Sidebar
st.sidebar.markdown("### Aparência e Acessibilidade")
tema_opcao = st.sidebar.radio(
    "Modo de Exibição",
    ["Claro (Off-white / Bege / Azul Pastel)", "Escuro (Slate Navy / Azul Pastel)"],
    index=0 if st.session_state.theme == "light" else 1,
    label_visibility="collapsed"
)
st.session_state.theme = "dark" if "Escuro" in tema_opcao else "light"
IS_DARK = st.session_state.theme == "dark"

# Definição dos Tokens de Cores (Paleta Azul Pastel, Bege/Off-white e Alto Contraste WCAG)
if not IS_DARK:
    # --- TEMA CLARO ---
    c_bg = "#fbfbfa"                  # Fundo principal off-white linho
    c_sidebar_bg = "#f5f3ee"          # Sidebar bege suave
    c_card_bg = "#ffffff"             # Fundo dos cartões em branco puro
    c_card_border = "#e2ded4"         # Borda suave tom areia/bege
    c_card_hover = "#d3cdbf"
    c_text_primary = "#182230"        # Títulos e números em grafite marinho (contraste 14:1)
    c_text_secondary = "#3b4758"      # Texto de corpo de alta legibilidade (contraste 7:1)
    c_text_muted = "#5a687d"          # Labels e subtítulos (contraste > 4.8:1)
    c_header_bg = "linear-gradient(135deg, #2d4563 0%, #3d597a 100%)" # Azul marinho ardósia
    c_header_text = "#ffffff"
    c_header_sub = "#e2e8f0"
    c_badge_bg = "#edf3f9"
    c_badge_text = "#244265"
    c_kpi_val = "#162333"
    c_delta_pos = "#1e724b"           # Verde sálvia contrastante
    c_delta_neg = "#a82828"           # Vermelho terracota contrastante
    c_sim_card_bg = "linear-gradient(135deg, #ffffff 0%, #f4f6fa 100%)"
    c_sim_card_border = "#4a729c"
    c_footer_bg = "#ffffff"
    c_footer_border = "#e2ded4"
    
    # Plotly Tokens (Claro)
    p_primary = "#4a729c"            # Azul pastel clássico
    p_secondary = "#c4b5a5"          # Bege areia suave
    p_accent = "#6b93c0"             # Azul pastel suave
    p_grid = "#eae6de"
    p_font = "#182230"
    p_colorscale = [(0, "#e8eef6"), (0.5, "#7b9ec3"), (1, "#2c486a")]
    p_gauge_bar = "#3d648f"
    p_steps_gauge = [
        {'range': [0, 10], 'color': '#f9dede'},
        {'range': [10, 30], 'color': '#f8ebd5'},
        {'range': [30, 60], 'color': '#e2ecf7'},
        {'range': [60, 100], 'color': '#daf0e4'}
    ]
else:
    # --- TEMA ESCURO ---
    c_bg = "#0d131a"                  # Fundo escuro slate navy
    c_sidebar_bg = "#131b24"          # Sidebar ardósia escura
    c_card_bg = "#182230"             # Fundo dos cartões em ardósia nítido
    c_card_border = "#2a3b50"         # Borda contrastante
    c_card_hover = "#3c506b"
    c_text_primary = "#f8fafc"        # Títulos quase brancos (contraste 15:1)
    c_text_secondary = "#e2e8f0"      # Texto de corpo claro e legível
    c_text_muted = "#94a3b8"          # Labels e subtítulos
    c_header_bg = "linear-gradient(135deg, #131b26 0%, #1e293b 100%)"
    c_header_text = "#f8fafc"
    c_header_sub = "#94a3b8"
    c_badge_bg = "#223347"
    c_badge_text = "#a3c8f3"
    c_kpi_val = "#f8fafc"
    c_delta_pos = "#4ade80"           # Verde pastel
    c_delta_neg = "#f87171"           # Vermelho pastel
    c_sim_card_bg = "linear-gradient(135deg, #182230 0%, #1c2838 100%)"
    c_sim_card_border = "#7ea5d6"
    c_footer_bg = "#182230"
    c_footer_border = "#2a3b50"
    
    # Plotly Tokens (Escuro)
    p_primary = "#7ea5d6"            # Azul pastel iluminado
    p_secondary = "#d4a373"          # Bege/areia iluminado
    p_accent = "#9bbce5"             # Azul pastel suave
    p_grid = "#28384d"
    p_font = "#f8fafc"
    p_colorscale = [(0, "#1c2a3a"), (0.5, "#416086"), (1, "#7ea5d6")]
    p_gauge_bar = "#7ea5d6"
    p_steps_gauge = [
        {'range': [0, 10], 'color': '#422424'},
        {'range': [10, 30], 'color': '#443422'},
        {'range': [30, 60], 'color': '#1e334a'},
        {'range': [60, 100], 'color': '#1c3e2e'}
    ]

# Injeção de CSS Dinâmico
CUSTOM_CSS = f"""
<style>
    /* Estilização Geral do App */
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
        background-color: {c_bg} !important;
        color: {c_text_secondary} !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    
    /* Barra Lateral */
    section[data-testid="stSidebar"] {{
        background-color: {c_sidebar_bg} !important;
        border-right: 1px solid {c_card_border} !important;
    }}
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] span {{
        color: {c_text_secondary} !important;
        font-weight: 500;
    }}
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {{
        color: {c_text_primary} !important;
    }}
    
    /* Header Principal */
    .app-header {{
        background: {c_header_bg};
        color: {c_header_text};
        padding: 1.8rem 2.2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border: 1px solid {c_card_border};
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
    }}
    .app-header h1 {{
        margin: 0;
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: {c_header_text} !important;
    }}
    .app-header p {{
        margin: 0.5rem 0 0 0;
        font-size: 1.05rem;
        color: {c_header_sub};
        line-height: 1.5;
    }}
    
    /* Badges */
    .badge {{
        display: inline-block;
        padding: 0.3rem 0.75rem;
        font-size: 0.8rem;
        font-weight: 600;
        border-radius: 6px;
        margin-right: 0.5rem;
        margin-top: 0.75rem;
        background-color: {c_badge_bg};
        color: {c_badge_text};
        border: 1px solid {c_card_border};
    }}
    
    /* Cartões de KPI */
    .kpi-card {{
        background-color: {c_card_bg};
        border: 1px solid {c_card_border};
        border-radius: 10px;
        padding: 1.25rem 1.4rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, border-color 0.15s ease;
        margin-bottom: 1rem;
        min-height: 125px;
    }}
    .kpi-card:hover {{
        border-color: {c_card_hover};
        transform: translateY(-2px);
    }}
    .kpi-title {{
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: {c_text_muted};
        margin-bottom: 0.35rem;
    }}
    .kpi-value {{
        font-size: 1.85rem;
        font-weight: 700;
        color: {c_kpi_val};
        line-height: 1.2;
    }}
    .kpi-subtitle {{
        font-size: 0.82rem;
        color: {c_text_muted};
        margin-top: 0.4rem;
    }}
    
    /* Painéis e Cards de Conteúdo */
    .content-card {{
        background-color: {c_card_bg};
        border: 1px solid {c_card_border};
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        margin-bottom: 1.5rem;
    }}
    
    /* Simulador */
    .sim-result-card {{
        background: {c_sim_card_bg};
        border: 2px solid {c_sim_card_border};
        border-radius: 12px;
        padding: 1.6rem;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
    }}
    
    /* Abas */
    button[data-baseweb="tab"] {{
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        padding: 0.65rem 1.2rem !important;
        color: {c_text_muted} !important;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        color: {c_text_primary} !important;
        border-bottom-color: {p_primary} !important;
    }}
    
    /* Títulos gerais */
    h1, h2, h3, h4 {{
        color: {c_text_primary} !important;
        font-weight: 700 !important;
    }}
    
    /* Dataframe e Tabelas */
    [data-testid="stDataFrame"] {{
        border: 1px solid {c_card_border};
        border-radius: 8px;
    }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def apply_chart_style(fig, height=420):
    """Aplica o design system unificado, paleta pastel e contraste acessível aos gráficos Plotly."""
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
            color=p_font,
            size=11
        ),
        margin=dict(l=25, r=20, t=35, b=25),
        xaxis=dict(
            gridcolor=p_grid,
            zerolinecolor=p_grid,
            tickfont=dict(color=p_font)
        ),
        yaxis=dict(
            gridcolor=p_grid,
            zerolinecolor=p_grid,
            tickfont=dict(color=p_font)
        )
    )
    return fig

# ==============================================================================
# 3. CAMADA DE CARGA E CACHE DE DADOS
# ==============================================================================
@st.cache_data(show_spinner=False)
def load_analytical_data():
    """Carrega a base analítica de 2,68M de registros em formato Parquet com colunas calculadas."""
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "enem_2023_analitico.parquet")
    if not os.path.exists(file_path):
        file_path = "data/processed/enem_2023_analitico.parquet"
        
    df = pd.read_parquet(file_path)
    
    # 1. Nota Média Geral
    df['nu_nota_media_geral'] = (
        df['NU_NOTA_CN'] + df['NU_NOTA_CH'] + df['NU_NOTA_LC'] + df['NU_NOTA_MT'] + df['NU_NOTA_REDACAO']
    ) / 5.0
    
    # 2. Flag de Alto Desempenho (Top 20% - P80 = 623.04 pts)
    df['fl_alto_desempenho'] = (df['nu_nota_media_geral'] >= 623.04).astype(np.int8)
    
    # 3. Classes de Renda
    renda_map = {
        'A': 'Baixa', 'B': 'Baixa', 'C': 'Baixa',
        'D': 'Média', 'E': 'Média', 'F': 'Média', 'G': 'Média',
        'H': 'Alta', 'I': 'Alta', 'J': 'Alta', 'K': 'Alta', 'L': 'Alta', 'M': 'Alta', 'N': 'Alta', 'O': 'Alta', 'P': 'Alta', 'Q': 'Alta'
    }
    df['classe_renda'] = df['Q006'].astype(str).map(renda_map).astype('category')
    
    # 4. Flags Derivadas
    df['in_vulnerabilidade'] = ((df['classe_renda'] == 'Baixa') & (df['Q025'].astype(str) == 'A')).astype(np.int8)
    df['in_idade_regular'] = (df['TP_FAIXA_ETARIA'] <= 3).astype(np.int8)
    
    return df

@st.cache_resource(show_spinner=False)
def load_trained_models():
    """Carrega os modelos serializados de Machine Learning da Sprint 5."""
    base_dir = os.path.dirname(__file__)
    reg_path = os.path.join(base_dir, "..", "models", "regressor_enem2023.joblib")
    clf_path = os.path.join(base_dir, "..", "models", "classificador_enem2023.joblib")
    
    if not os.path.exists(reg_path):
        reg_path = "models/regressor_enem2023.joblib"
        clf_path = "models/classificador_enem2023.joblib"
        
    reg_model = joblib.load(reg_path)
    clf_model = joblib.load(clf_path)
    return reg_model, clf_model

# ==============================================================================
# 4. CARGA INICIAL
# ==============================================================================
with st.spinner("Carregando microdados do ENEM 2023..."):
    df_raw = load_analytical_data()
    reg_pipeline, clf_pipeline = load_trained_models()

TOTAL_POPULACAO = 3933955
TOTAL_ANALITICO = len(df_raw)  # 2.678.264
MEDIA_NACIONAL = float(df_raw['nu_nota_media_geral'].mean())
P80_NACIONAL = 623.04

# ==============================================================================
# 5. BARRA LATERAL (SIDEBAR) — FILTROS DINÂMICOS
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.markdown("### Filtros da Base")

# Filtro 1: Região / UF
regioes_disponiveis = ["Todas"] + sorted(list(df_raw['regiao'].dropna().unique()))
sel_regiao = st.sidebar.selectbox("Macrorregião", regioes_disponiveis, index=0)

if sel_regiao != "Todas":
    ufs_da_regiao = sorted(list(df_raw[df_raw['regiao'] == sel_regiao]['SG_UF_PROVA'].dropna().unique()))
else:
    ufs_da_regiao = sorted(list(df_raw['SG_UF_PROVA'].dropna().unique()))
    
ufs_disponiveis = ["Todas"] + ufs_da_regiao
sel_uf = st.sidebar.selectbox("Estado (UF)", ufs_disponiveis, index=0)

# Filtro 2: Tipo de Escola
escolas_disponiveis = ["Todas", "Pública", "Privada"]
sel_escola = st.sidebar.selectbox("Rede de Ensino", escolas_disponiveis, index=0)

# Filtro 3: Classe de Renda
rendas_disponiveis = ["Todas", "Baixa (Até 1,5 SM)", "Média (1,5 a 4 SM)", "Alta (> 4 SM)"]
sel_renda = st.sidebar.selectbox("Faixa de Renda Familiar", rendas_disponiveis, index=0)

# Filtro 4: Internet
internet_disponiveis = ["Todos", "Com internet", "Sem internet"]
sel_internet = st.sidebar.selectbox("Acesso à Internet", internet_disponiveis, index=0)

# Filtro 5: Sexo
sexos_disponiveis = ["Todos", "Feminino", "Masculino"]
sel_sexo = st.sidebar.selectbox("Sexo", sexos_disponiveis, index=0)

# Filtro 6: Cor / Raça
racas_disponiveis = ["Todas"] + [r for r in df_raw['cor_raca_desc'].unique() if r != 'Não declarado']
sel_raca = st.sidebar.selectbox("Cor / Raça", racas_disponiveis, index=0)

st.sidebar.markdown("---")

# Aplicação dos Filtros
df_filtered = df_raw.copy()

if sel_regiao != "Todas":
    df_filtered = df_filtered[df_filtered['regiao'] == sel_regiao]
if sel_uf != "Todas":
    df_filtered = df_filtered[df_filtered['SG_UF_PROVA'] == sel_uf]
if sel_escola != "Todas":
    df_filtered = df_filtered[df_filtered['escola_desc'] == sel_escola]
if sel_renda != "Todas":
    mapa_filtro_renda = {
        "Baixa (Até 1,5 SM)": "Baixa",
        "Média (1,5 a 4 SM)": "Média",
        "Alta (> 4 SM)": "Alta"
    }
    df_filtered = df_filtered[df_filtered['classe_renda'] == mapa_filtro_renda[sel_renda]]
if sel_internet != "Todos":
    df_filtered = df_filtered[df_filtered['internet_desc'] == sel_internet]
if sel_sexo != "Todos":
    df_filtered = df_filtered[df_filtered['sexo_desc'] == sel_sexo]
if sel_raca != "Todas":
    df_filtered = df_filtered[df_filtered['cor_raca_desc'] == sel_raca]

# Resumo da Amostra Filtrada na Sidebar
n_filtrado = len(df_filtered)
pct_base = (n_filtrado / TOTAL_ANALITICO) * 100

st.sidebar.markdown(f"""
<div style="background-color: {c_card_bg}; border: 1px solid {c_card_border}; color: {c_text_primary}; padding: 1.1rem; border-radius: 8px;">
    <div style="font-size: 0.75rem; text-transform: uppercase; color: {c_text_muted}; font-weight: 600; letter-spacing: 0.05em;">Amostra Selecionada</div>
    <div style="font-size: 1.35rem; font-weight: 700; color: {p_primary}; margin: 0.2rem 0;">{n_filtrado:,} candidatos</div>
    <div style="font-size: 0.8rem; color: {c_text_muted};">Representa <b>{pct_base:.1f}%</b> da base analítica</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<br/>", unsafe_allow_html=True)
st.sidebar.caption("EduDataBR • Microdados Oficiais INEP 2023 • Streamlit & Scikit-Learn.")

# ==============================================================================
# 6. CABEÇALHO DA APLICAÇÃO
# ==============================================================================
st.markdown(f"""
<div class="app-header">
    <h1>EduDataBR — Panorama & Inteligência Preditiva ENEM 2023</h1>
    <p>Plataforma analítica e preditiva sobre determinantes socioeconômicos e educacionais do desempenho no exame nacional.</p>
    <div>
        <span class="badge">Microdados Oficiais INEP 2023</span>
        <span class="badge">N = 2.678.264 Casos Analíticos</span>
        <span class="badge">Machine Learning & Explicabilidade</span>
    </div>
</div>
""", unsafe_allow_html=True)

if n_filtrado == 0:
    st.warning("Nenhum participante encontrado para a combinação de filtros selecionada. Por favor, ajuste os parâmetros na barra lateral.")
    st.stop()

# ==============================================================================
# 7. NAVEGAÇÃO PRINCIPAL POR ABAS (DESIGN MINIMALISTA & LIMPO)
# ==============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Visão Geral & Demografia",
    "Desigualdades Socioeducacionais",
    "Geografia da Educação",
    "Simulador Preditivo (What-If)",
    "Metodologia & Governança"
])

# ------------------------------------------------------------------------------
# ABA 1: VISÃO GERAL & DEMOGRAFIA
# ------------------------------------------------------------------------------
with tab1:
    st.markdown("### Indicadores Principais de Desempenho")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    media_filtro = df_filtered['nu_nota_media_geral'].mean()
    delta_media = media_filtro - MEDIA_NACIONAL
    pct_alto_desempenho = (df_filtered['fl_alto_desempenho'].mean()) * 100
    taxa_zero_redacao = (df_filtered['fl_redacao_zero'].mean()) * 100
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Candidatos no Filtro</div>
            <div class="kpi-value">{n_filtrado:,}</div>
            <div class="kpi-subtitle">{pct_base:.1f}% da base completa</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        sinal = "+" if delta_media >= 0 else ""
        cor_delta = c_delta_pos if delta_media >= 0 else c_delta_neg
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Nota Média Geral</div>
            <div class="kpi-value">{media_filtro:.1f} pts</div>
            <div class="kpi-subtitle" style="color: {cor_delta}; font-weight: 600;">{sinal}{delta_media:.1f} pts vs. Brasil ({MEDIA_NACIONAL:.1f})</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Nota de Corte (P80)</div>
            <div class="kpi-value">{P80_NACIONAL:.1f} pts</div>
            <div class="kpi-subtitle">Limiar do Top 20% Nacional</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Taxa de Excelência</div>
            <div class="kpi-value">{pct_alto_desempenho:.1f}%</div>
            <div class="kpi-subtitle">Alcançaram o Top 20%</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Taxa Zero na Redação</div>
            <div class="kpi-value">{taxa_zero_redacao:.2f}%</div>
            <div class="kpi-subtitle">{(df_filtered['fl_redacao_zero'].sum()):,} notas zero</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Linha de Gráficos: Distribuição das Provas e Perfil Étnico-Racial
    gcol1, gcol2 = st.columns([3, 2])
    
    with gcol1:
        st.markdown("#### Distribuição das Notas no Grupo Selecionado")
        prova_selecionada = st.selectbox(
            "Selecione a Prova para Visualizar:",
            ["Média Geral", "Matemática (MT)", "Redação", "Linguagens e Códigos (LC)", "Ciências Humanas (CH)", "Ciências da Natureza (CN)"],
            index=0
        )
        
        mapa_colunas_provas = {
            "Média Geral": "nu_nota_media_geral",
            "Matemática (MT)": "NU_NOTA_MT",
            "Redação": "NU_NOTA_REDACAO",
            "Linguagens e Códigos (LC)": "NU_NOTA_LC",
            "Ciências Humanas (CH)": "NU_NOTA_CH",
            "Ciências da Natureza (CN)": "NU_NOTA_CN"
        }
        col_plot = mapa_colunas_provas[prova_selecionada]
        
        # Amostragem para fluidez na interface
        sample_size = min(len(df_filtered), 40000)
        df_sample = df_filtered.sample(sample_size, random_state=42) if len(df_filtered) > 40000 else df_filtered
        
        fig_hist = px.histogram(
            df_sample,
            x=col_plot,
            nbins=60,
            marginal="box",
            opacity=0.85,
            color_discrete_sequence=[p_primary],
            labels={col_plot: f"Nota em {prova_selecionada}"}
        )
        fig_hist.add_vline(
            x=df_filtered[col_plot].mean(),
            line_dash="dash",
            line_color=c_delta_neg,
            annotation_text=f"Média: {df_filtered[col_plot].mean():.1f} pts",
            annotation_font_color=p_font
        )
        apply_chart_style(fig_hist, height=430)
        fig_hist.update_layout(xaxis_title="Pontuação", yaxis_title="Frequência")
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with gcol2:
        st.markdown("#### Composição Étnico-Racial")
        df_raca = df_filtered['cor_raca_desc'].value_counts().reset_index()
        df_raca.columns = ['Cor / Raça', 'Total']
        
        # Cores suaves e acessíveis para categorias
        cores_raca = [p_primary, p_secondary, "#6b92be", "#8a9ba8", "#5b9279", "#b56576"]
        
        fig_raca = px.pie(
            df_raca,
            names='Cor / Raça',
            values='Total',
            hole=0.48,
            color_discrete_sequence=cores_raca
        )
        apply_chart_style(fig_raca, height=430)
        fig_raca.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.28, font=dict(color=p_font)))
        st.plotly_chart(fig_raca, use_container_width=True)

# ------------------------------------------------------------------------------
# ABA 2: DESIGUALDADES SOCIOEDUCACIONAIS
# ------------------------------------------------------------------------------
with tab2:
    st.markdown("### O Impacto Estrutural da Renda, Conectividade e Rede de Ensino")
    st.markdown("Análise comparativa das disparidades de desempenho no exame nacional à luz dos dados contextuais declarados.")
    
    dcol1, dcol2 = st.columns(2)
    
    with dcol1:
        st.markdown("#### Desempenho Médio por Faixa de Renda Familiar")
        
        df_renda_agg = df_filtered.groupby('renda_desc', observed=True).agg(
            media_geral=('nu_nota_media_geral', 'mean'),
            total=('nu_nota_media_geral', 'count')
        ).reset_index()
        
        fig_renda = px.bar(
            df_renda_agg,
            x='media_geral',
            y='renda_desc',
            orientation='h',
            text=df_renda_agg['media_geral'].apply(lambda x: f"{x:.1f}"),
            color='media_geral',
            color_continuous_scale=p_colorscale,
            labels={'media_geral': 'Nota Média Geral', 'renda_desc': 'Faixa de Renda Familiar'}
        )
        fig_renda.add_vline(
            x=MEDIA_NACIONAL,
            line_dash="dash",
            line_color=c_delta_neg,
            annotation_text=f"Média Brasil ({MEDIA_NACIONAL:.1f})",
            annotation_font_color=p_font
        )
        apply_chart_style(fig_renda, height=480)
        fig_renda.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_renda, use_container_width=True)
        
    with dcol2:
        st.markdown("#### Efeito da Internet Domiciliar por Classe de Renda")
        df_inter_agg = df_filtered.groupby(['classe_renda', 'internet_desc'], observed=True)['nu_nota_media_geral'].mean().reset_index()
        
        fig_inter = px.bar(
            df_inter_agg,
            x='classe_renda',
            y='nu_nota_media_geral',
            color='internet_desc',
            barmode='group',
            text=df_inter_agg['nu_nota_media_geral'].apply(lambda x: f"{x:.1f}"),
            color_discrete_map={'Com internet': p_primary, 'Sem internet': p_secondary},
            labels={'nu_nota_media_geral': 'Nota Média Geral', 'classe_renda': 'Classe de Renda', 'internet_desc': 'Conectividade'}
        )
        apply_chart_style(fig_inter, height=480)
        fig_inter.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color=p_font)))
        st.plotly_chart(fig_inter, use_container_width=True)
        
    st.markdown("---")
    
    dcol3, dcol4 = st.columns(2)
    
    with dcol3:
        st.markdown("#### Diferencial entre Escola Pública e Privada por Área")
        areas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
        nomes_areas = ['Ciências Natureza', 'Ciências Humanas', 'Linguagens', 'Matemática', 'Redação']
        
        df_escola_pub_priv = df_filtered[df_filtered['escola_desc'].isin(['Pública', 'Privada'])]
        if len(df_escola_pub_priv) > 0:
            df_escola_agg = df_escola_pub_priv.groupby('escola_desc', observed=True)[areas].mean().T.reset_index()
            df_escola_agg.columns = ['Área', 'Pública', 'Privada']
            df_escola_agg['Área'] = nomes_areas
            
            fig_gap = go.Figure()
            fig_gap.add_trace(go.Bar(
                x=df_escola_agg['Área'],
                y=df_escola_agg['Pública'],
                name='Escola Pública',
                marker_color='#708090',
                text=df_escola_agg['Pública'].apply(lambda x: f"{x:.1f}"),
                textposition='auto'
            ))
            fig_gap.add_trace(go.Bar(
                x=df_escola_agg['Área'],
                y=df_escola_agg['Privada'],
                name='Escola Privada',
                marker_color=p_primary,
                text=df_escola_agg['Privada'].apply(lambda x: f"{x:.1f}"),
                textposition='auto'
            ))
            apply_chart_style(fig_gap, height=420)
            fig_gap.update_layout(
                barmode='group',
                yaxis_title="Nota Média",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color=p_font))
            )
            st.plotly_chart(fig_gap, use_container_width=True)
        else:
            st.info("O filtro atual não contém participantes de escolas públicas e privadas para comparação.")
            
    with dcol4:
        st.markdown("#### Incidência de Notas Zero na Redação por Rede")
        if len(df_escola_pub_priv) > 0:
            df_zero_agg = df_escola_pub_priv.groupby('escola_desc', observed=True)['fl_redacao_zero'].mean().reset_index()
            df_zero_agg['Taxa Zero (%)'] = df_zero_agg['fl_redacao_zero'] * 100
            
            fig_zero = px.bar(
                df_zero_agg,
                x='escola_desc',
                y='Taxa Zero (%)',
                text=df_zero_agg['Taxa Zero (%)'].apply(lambda x: f"{x:.2f}%"),
                color='escola_desc',
                color_discrete_map={'Pública': '#a82828' if not IS_DARK else '#f87171', 'Privada': p_primary},
                labels={'escola_desc': 'Rede Escolar', 'Taxa Zero (%)': 'Taxa de Zeros (%)'}
            )
            apply_chart_style(fig_zero, height=420)
            fig_zero.update_layout(showlegend=False)
            st.plotly_chart(fig_zero, use_container_width=True)

# ------------------------------------------------------------------------------
# ABA 3: GEOGRAFIA DA EDUCAÇÃO
# ------------------------------------------------------------------------------
with tab3:
    st.markdown("### Análise Espacial e Ranking Federativo do ENEM 2023")
    st.markdown("Comparativo do desempenho educacional entre as 27 Unidades Federativas e as 5 Macrorregiões.")
    
    # Agregação por UF
    df_uf_agg = df_filtered.groupby('SG_UF_PROVA', observed=True).agg(
        media_geral=('nu_nota_media_geral', 'mean'),
        media_mt=('NU_NOTA_MT', 'mean'),
        media_red=('NU_NOTA_REDACAO', 'mean'),
        taxa_alto_desemp=('fl_alto_desempenho', 'mean'),
        total_inscritos=('nu_nota_media_geral', 'count')
    ).reset_index()
    
    uf_regiao_map = df_raw[['SG_UF_PROVA', 'regiao']].drop_duplicates().set_index('SG_UF_PROVA')['regiao'].to_dict()
    df_uf_agg['Região'] = df_uf_agg['SG_UF_PROVA'].map(uf_regiao_map)
    df_uf_agg['taxa_alto_desemp'] = df_uf_agg['taxa_alto_desemp'] * 100
    df_uf_agg = df_uf_agg.sort_values('media_geral', ascending=True)
    
    # Cores harmonizadas por macrorregião (pastel acessível)
    cores_regiao = {
        'Sudeste': '#3b628a' if not IS_DARK else '#7ea5d6',
        'Sul': '#547c9f' if not IS_DARK else '#92b4dc',
        'Centro-Oeste': '#5b9279' if not IS_DARK else '#7ec2a5',
        'Nordeste': '#c4a275' if not IS_DARK else '#dfbd92',
        'Norte': '#b56576' if not IS_DARK else '#e58273'
    }
    
    fig_uf = px.bar(
        df_uf_agg,
        x='media_geral',
        y='SG_UF_PROVA',
        orientation='h',
        color='Região',
        text=df_uf_agg['media_geral'].apply(lambda x: f"{x:.1f}"),
        color_discrete_map=cores_regiao,
        labels={'media_geral': 'Nota Média Geral', 'SG_UF_PROVA': 'Unidade Federativa'}
    )
    fig_uf.add_vline(
        x=MEDIA_NACIONAL,
        line_dash="dash",
        line_color=c_delta_neg,
        annotation_text=f"Média Nacional ({MEDIA_NACIONAL:.1f})",
        annotation_font_color=p_font
    )
    apply_chart_style(fig_uf, height=660)
    fig_uf.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(color=p_font)))
    st.plotly_chart(fig_uf, use_container_width=True)
    
    st.markdown("#### Tabela Analítica Completa por Estado")
    df_uf_table = df_uf_agg.sort_values('media_geral', ascending=False).reset_index(drop=True)
    df_uf_table.columns = ['UF', 'Média Geral (pts)', 'Média Matemática', 'Média Redação', 'Taxa Top 20% (%)', 'Participantes', 'Região']
    
    st.dataframe(
        df_uf_table.style.format({
            'Média Geral (pts)': '{:.2f}',
            'Média Matemática': '{:.2f}',
            'Média Redação': '{:.2f}',
            'Taxa Top 20% (%)': '{:.2f}%',
            'Participantes': '{:,}'
        }),
        use_container_width=True,
        height=320
    )

# ------------------------------------------------------------------------------
# ABA 4: SIMULADOR PREDITIVO (WHAT-IF ANALYSIS)
# ------------------------------------------------------------------------------
with tab4:
    st.markdown("### Simulador Preditivo de Desempenho (What-If Analysis)")
    st.markdown(r"""
    Este simulador utiliza os modelos de Machine Learning treinados e validados na **Sprint 5** (`HistGradientBoostingRegressor` e `HistGradientBoostingClassifier`).
    
    Selecione abaixo as características contextuais de um perfil hipotético para estimar a nota média esperada e a probabilidade de aprovação no Top 20% nacional ($P_{80} \ge 623$ pontos).
    """)
    
    sim_col1, sim_col2 = st.columns([1, 1], gap="large")
    
    with sim_col1:
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.markdown("#### Configuração do Perfil do Estudante")
        
        sim_escola = st.selectbox("1. Rede de Ensino:", ["Pública", "Privada", "Não respondeu"], index=0)
        
        mapa_q006_labels = {
            'A': 'A — Nenhuma Renda (R$ 0)',
            'B': 'B — Até R$ 1.320 (Até 1 Salário Mínimo)',
            'C': 'C — R$ 1.320 a 1.980 (1 a 1,5 SM)',
            'D': 'D — R$ 1.980 a 2.640 (1,5 a 2 SM)',
            'E': 'E — R$ 2.640 a 3.960 (2 a 3 SM)',
            'F': 'F — R$ 3.960 a 5.280 (3 a 4 SM)',
            'G': 'G — R$ 5.280 a 6.600 (4 a 5 SM)',
            'H': 'H — R$ 6.600 a 7.920 (5 a 6 SM)',
            'I': 'I — R$ 7.920 a 9.240 (6 a 7 SM)',
            'J': 'J — R$ 9.240 a 10.560 (7 a 8 SM)',
            'K': 'K — R$ 10.560 a 11.880 (8 a 9 SM)',
            'L': 'L — R$ 11.880 a 13.200 (9 a 10 SM)',
            'M': 'M — R$ 13.200 a 15.840 (10 a 12 SM)',
            'N': 'N — R$ 15.840 a 19.800 (12 a 15 SM)',
            'O': 'O — R$ 19.800 a 26.400 (15 a 20 SM)',
            'P': 'P — Mais de R$ 26.400 (> 20 SM)',
            'Q': 'Q — Mais de R$ 26.400 (> 20 SM)'
        }
        sim_q006_display = st.selectbox("2. Faixa de Renda Familiar:", list(mapa_q006_labels.values()), index=1)
        sim_q006 = sim_q006_display.split(' — ')[0]
        
        sim_internet = st.radio("3. Acesso Domiciliar à Internet:", ["Com internet", "Sem internet"], index=0, horizontal=True)
        
        sim_uf = st.selectbox(
            "4. Estado de Realização da Prova (UF):",
            sorted(list(df_raw['SG_UF_PROVA'].unique())),
            index=list(sorted(list(df_raw['SG_UF_PROVA'].unique()))).index('SP')
        )
        
        sim_idade = st.slider("5. Faixa Etária (anos):", min_value=15, max_value=40, value=17, step=1)
        
        scol_a, scol_b = st.columns(2)
        with scol_a:
            sim_sexo = st.selectbox("6. Sexo:", ["Feminino", "Masculino"], index=0)
        with scol_b:
            sim_raca = st.selectbox("7. Cor / Raça:", ["Parda", "Branca", "Preta", "Amarela", "Indígena"], index=0)
            
        st.markdown("</div>", unsafe_allow_html=True)
        
    with sim_col2:
        # Mapeamento do perfil simulado para o formato do Pipeline
        renda_map = {
            'A': 'Baixa', 'B': 'Baixa', 'C': 'Baixa',
            'D': 'Média', 'E': 'Média', 'F': 'Média', 'G': 'Média',
            'H': 'Alta', 'I': 'Alta', 'J': 'Alta', 'K': 'Alta', 'L': 'Alta', 'M': 'Alta', 'N': 'Alta', 'O': 'Alta', 'P': 'Alta', 'Q': 'Alta'
        }
        classe_renda_sim = renda_map[sim_q006]
        in_vulnerabilidade_sim = 1 if (classe_renda_sim == 'Baixa' and sim_internet == 'Sem internet') else 0
        in_idade_regular_sim = 1 if sim_idade <= 18 else 0
        
        # Mapeamento da idade para o padrão INEP
        if sim_idade < 17:
            tp_faixa_sim = 1
        elif sim_idade == 17:
            tp_faixa_sim = 2
        elif sim_idade == 18:
            tp_faixa_sim = 3
        elif sim_idade == 19:
            tp_faixa_sim = 4
        elif sim_idade == 20:
            tp_faixa_sim = 5
        elif sim_idade == 21:
            tp_faixa_sim = 6
        elif sim_idade == 22:
            tp_faixa_sim = 7
        elif sim_idade <= 25:
            tp_faixa_sim = 10
        elif sim_idade <= 30:
            tp_faixa_sim = 11
        else:
            tp_faixa_sim = 12
            
        regiao_sim = uf_regiao_map.get(sim_uf, 'Sudeste')
        
        sim_input_df = pd.DataFrame([{
            'TP_FAIXA_ETARIA': tp_faixa_sim,
            'in_idade_regular': in_idade_regular_sim,
            'in_vulnerabilidade': in_vulnerabilidade_sim,
            'escola_desc': sim_escola,
            'classe_renda': classe_renda_sim,
            'Q006': sim_q006,
            'SG_UF_PROVA': sim_uf,
            'regiao': regiao_sim,
            'cor_raca_desc': sim_raca,
            'sexo_desc': sim_sexo,
            'internet_desc': sim_internet
        }])
        
        # Execução da Inferência
        pred_nota = float(reg_pipeline.predict(sim_input_df)[0])
        pred_prob_top20 = float(clf_pipeline.predict_proba(sim_input_df)[0, 1]) * 100
        
        st.markdown("<div class='sim-result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {p_primary}; margin-top: 0;'>Resultado da Inferência Preditiva</h3>", unsafe_allow_html=True)
        
        scard_1, scard_2 = st.columns(2)
        with scard_1:
            delta_sim = pred_nota - MEDIA_NACIONAL
            sinal_sim = "+" if delta_sim >= 0 else ""
            st.metric("Nota Média Estimada", f"{pred_nota:.1f} pts", f"{sinal_sim}{delta_sim:.1f} pts vs. Brasil")
            
        with scard_2:
            st.metric("Probabilidade Top 20%", f"{pred_prob_top20:.1f}%", f"{pred_prob_top20 - 20:.1f}% vs. Baseline")
            
        st.markdown("---")
        
        # Gráfico Gauge de Probabilidade
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred_prob_top20,
            title={'text': "Probabilidade de Atingir o Top 20% Nacional (P80)", 'font': {'size': 13, 'color': p_font}},
            number={'suffix': "%", 'font': {'size': 26, 'color': p_font}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': c_text_muted},
                'bar': {'color': p_gauge_bar},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 1,
                'bordercolor': c_card_border,
                'steps': p_steps_gauge,
                'threshold': {
                    'line': {'color': c_delta_neg, 'width': 3},
                    'thickness': 0.75,
                    'value': 20.0
                }
            }
        ))
        apply_chart_style(fig_gauge, height=260)
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # Diagnóstico Contextualizado
        st.markdown(f"<div style='text-align: left; font-size: 0.9rem; color: {c_text_secondary}; line-height: 1.5;'>", unsafe_allow_html=True)
        st.markdown("**Diagnóstico do Perfil Avaliado:**")
        if pred_nota >= 600:
            st.success(f"O perfil apresenta forte impulso contextual. Estima-se pontuação entre **{pred_nota-80:.0f} e {pred_nota+80:.0f} pontos**, com probabilidade elevada ({pred_prob_top20:.1f}%) de disputar vagas em cursos de alta concorrência.")
        elif pred_nota >= 520:
            st.info(f"O perfil situa-se na faixa média nacional (**{pred_nota-80:.0f} a {pred_nota+80:.0f} pontos**). O acesso a cursos concorridos dependerá primariamente do engajamento individual nas áreas de Matemática e Redação.")
        else:
            st.warning(f"O perfil reflete severas barreiras socioeconômicas (pontuação esperada de **{pred_nota-80:.0f} a {pred_nota+80:.0f} pontos**). A chance de atingir o topo 20% é reduzida ({pred_prob_top20:.1f}%), reforçando a relevância de políticas de cotas e equidade educacional.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ABA 5: METODOLOGIA, HIPÓTESES & GOVERNANÇA
# ------------------------------------------------------------------------------
with tab5:
    st.markdown("### Metodologia, Testes Estatísticos e Governança Técnica")
    
    mcol1, mcol2 = st.columns(2)
    
    with mcol1:
        st.markdown("#### Síntese dos Testes de Hipóteses Estatísticas")
        st.markdown(r"""
        Todas as hipóteses foram avaliadas pelo **Tamanho do Efeito (*Effect Size*)** para evitar conclusões espúrias decorrentes do tamanho amostral massivo ($N > 2{,}6\text{M}$):
        
        - **H1 (Renda e Matemática):** **[Confirmada]** Forte correlação monotônica ($\rho = 0{,}457, p < 0{,}001$), com gap de $+231{,}2$ pontos entre extremos de renda.
        - **H2 (Internet e Desempenho):** **[Confirmada]** Mesmo no estrato de baixa renda ($\le 1$ SM), a conectividade domiciliar adiciona $+23{,}6$ pontos em Matemática ($d = 0{,}23$).
        - **H3 (Escola Pública vs. Privada):** **[Confirmada]** Efeito muito grande. Alunos de rede privada superam os de pública em $+126{,}6$ pts em Matemática ($d = 1{,}05$) e $+150{,}5$ pts em Redação ($d = 0{,}84$).
        - **H4 (Disparidade de Gênero):** **[Confirmada]** Homens superam mulheres em Matemática ($+44{,}1$ pts, $d = 0{,}42$); mulheres superam homens em Redação ($+44{,}0$ pts, $d = 0{,}25$).
        - **H5 (Ceará em Matemática):** **[Refutada]** A média de Matemática no CE ($523{,}3$ pts) ficou ligeiramente abaixo da média nacional ($534{,}0$ pts, gap $-10{,}7$ pts).
        - **H6 (Evasão por Vulnerabilidade):** **[Refutada no Limiar Prático]** Embora a evasão no Dia 2 seja maior em vulneráveis ($5{,}94\%$ vs $4{,}73\%$), o *Odds Ratio* ($1{,}28\times$) não atingiu o limiar pragmático estabelecido a priori ($1{,}5\times$).
        """)
        
    with mcol2:
        st.markdown("#### Registro de Decisões Técnicas de Engenharia (ADRs)")
        st.markdown(r"""
        - **ADR-01/02:** Manutenção de notas zero (Redação: 93,1k; Objetivas: 19,5k) com flags indicadoras, preservando o fenômeno socioeducacional da evasão de conteúdo.
        - **ADR-04:** Armazenamento colunar em **Apache Parquet** (`enem_2023_analitico.parquet`), reduzindo o tempo de leitura de $5{,}7\text{s}$ para $0{,}2\text{s}$ e uso de memória em $67\%$.
        - **ADR-05:** Primazia do *Effect Size* ($d$ de Cohen, $\rho$ de Spearman, *Odds Ratio*) sobre o valor-p na validação de hipóteses.
        - **ADR-07:** Target de classificação definido pelo **Percentil 80 Nacional** ($P_{80} = 623{,}04$ pts), garantindo classe balanceada ($20/80$) para mensuração por PR-AUC.
        - **ADR-08:** Blindagem absoluta contra *Data Leakage* (zero notas parciais na matriz $X$, encoders ajustados estritamente na partição de treino).
        - **ADR-09:** Uso do `HistGradientBoosting` com binning em histogramas, permitindo treinar sobre 2,14 milhões de amostras em menos de 35 segundos.
        - **ADR-10:** Explicabilidade com **SHAP Values** (`TreeExplainer`) calculado sobre amostra estatística representativa ($N = 5.000$) do conjunto de teste.
        - **ADR-11/12/13:** Arquitetura Streamlit em página única com navegação em abas horizontais, cache duplo (`@st.cache_data` e `@st.cache_resource`) e paleta acessível adaptável claro/escuro.
        """)
        
    st.markdown("---")
    st.markdown(f"""
    <div style="background-color: {c_footer_bg}; border: 1px solid {c_footer_border}; padding: 1.2rem; border-radius: 8px; text-align: center; color: {c_text_muted}; font-size: 0.85rem;">
        <b>EduDataBR — Análise de Dados Educacionais & Inteligência Preditiva</b><br/>
        Desenvolvido por Gustavo Saraiva • Microdados Oficiais do ENEM 2023 (INEP/MEC) • Código Aberto no GitHub
    </div>
    """, unsafe_allow_html=True)
