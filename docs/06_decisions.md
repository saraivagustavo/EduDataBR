# 🏛️ Registro de Decisões Técnicas (ADR) — EduDataBR

## 1. Objetivo

Este documento registra as **Decisões Técnicas e Analíticas (Architectural and Analytical Decision Records)** tomadas ao longo do desenvolvimento do projeto **EduDataBR**.

O objetivo é manter a rastreabilidade das escolhas de engenharia, governança e modelagem de dados, justificando os critérios adotados e seus impactos no ciclo de vida dos dados.

---

## 2. Decisões da Sprint 4 (Limpeza & Análise Exploratória)

---

### ADR-01: Tratamento de Notas Zero na Redação
- **Contexto:** Entre os 2.678.264 participantes presentes em todas as 4 provas, **93.149** (3,48%) receberam nota zero na prova de Redação. Essa taxa atinge 4,96% em escolas públicas e apenas 0,81% em escolas privadas.
- **Decisão:** Manter os registros com nota zero na base analítica e criar a coluna booleana indicadora `fl_redacao_zero`.
- **Justificativa:** A nota zero na redação decorre de critérios regulamentares do edital (folha em branco, fuga total ao tema, extensão insuficiente, cópia de texto motivador). Trata-se de um fenômeno socioeducacional concreto e não de um erro de coleta. Descartar esses participantes falsearia a realidade da evasão de conteúdo e superestimaria a média de escolas públicas.
- **Impacto:** Nas visualizações e análises de sensibilidade, as métricas são apresentadas com e sem os zeros para fins comparativos.

---

### ADR-02: Tratamento de Notas Zero nas Provas Objetivas
- **Contexto:** 19.501 participantes (0,73% dos presentes totais) obtiveram nota zero em ao menos uma das quatro provas objetivas (TRI).
- **Decisão:** Manter os registros na base com a flag indicadora `fl_objetiva_zero`.
- **Justificativa:** O volume é marginal (< 1%) e não compromete a estabilidade das análises paramétricas gerais, mantendo a integridade da amostra completa de concluintes.

---

### ADR-03: Padronização e Nomenclatura do Notebook de Limpeza
- **Contexto:** No roadmap original havia divergência na nomenclatura do notebook (`02_limpeza_tratamento.ipynb` vs `02_limpeza_dados.ipynb`).
- **Decisão:** Padronizar e manter o arquivo existente [`notebooks/02_limpeza_dados.ipynb`](../notebooks/02_limpeza_dados.ipynb), atualizando as referências cruzadas na documentação oficial.

---

### ADR-04: Estratégia de Armazenamento e Leitura: Apache Parquet vs. PostgreSQL
- **Contexto:** O projeto opera com mais de 3,93 milhões de registros. A leitura direta do banco PostgreSQL via Python ou do CSV bruto exigia tempo excessivo e conexões ativas com o SGBD.
- **Decisão:**
  - O pipeline de limpeza gera duas bases otimizadas em formato colunar **Apache Parquet**:
    1. `data/processed/enem_2023_populacional.parquet` (N = 3.933.955, ~69 MB)
    2. `data/processed/enem_2023_analitico.parquet` (N = 2.678.264, ~48 MB)
  - O banco de dados PostgreSQL permanece como repositório corporativo e camada de **validação cruzada**.
- **Justificativa:** O formato Parquet reduziu o tempo de carregamento da base em Python de **5,7 segundos para 0,5 segundo** (mais de 10x mais rápido), preservando tipos categóricos, inteiros compactos (`int8`, `int16`) e decimais (`float32`), sem dependência de infraestrutura externa ativa durante o desenvolvimento de notebooks.

---

### ADR-05: Validação de Hipóteses Científicas pelo Tamanho do Efeito (*Effect Size*)
- **Contexto:** Com tamanhos amostrais gigantescos ($N > 2,6 \text{ milhões}$), o poder estatístico é quase infinito e qualquer diferença ínfima atinge $p < 0,001$.
- **Decisão:** Toda hipótese analítica deve ser avaliada prioritariamente pelo **Tamanho do Efeito** ($d$ de Cohen, $\rho$ de Spearman, $V$ de Cramér e *Odds Ratio*), e não apenas pela significância estatística do p-valor.
- **Impacto:** Permitiu classificar com rigor científico hipóteses com relevância substantiva (ex.: H3 com $d = 1,05$) e refutar hipóteses que não atingiram o limiar prático estabelecido a priori (ex.: H6 com $OR = 1,28\times$ vs limiar de $1,5\times$).

---

### ADR-06: Stack de Visualização de Dados por Fase do Projeto
- **Contexto:** Havia necessidade de definir a biblioteca gráfica padrão para relatórios técnicos versus produtos interativos.
- **Decisão:**
  - **Fase de Análise e Relatórios (Sprint 4):** Matplotlib e Seaborn para exportação de gráficos estáticos em alta resolução (PNG) salvos em `reports/figures/`, garantindo renderização instantânea no GitHub e em relatórios markdown.
  - **Fase de Aplicação (Sprint 6):** Plotly para gráficos dinâmicos e interativos integrados ao Streamlit.
