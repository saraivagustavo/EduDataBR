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

---

## 3. Decisões da Sprint 5 (Engenharia de Features & Machine Learning)

---

### ADR-07: Definição do Target de Classificação por Percentil Relativo (Top 20% — $P_{80}$)
- **Contexto:** Havia necessidade de definir um target binário para modelar a probabilidade de alta performance no ENEM, associada a notas de corte de cursos concorridos em universidades públicas.
- **Decisão:** Adotar como nota de corte o **Percentil 80 da nota média geral nacional** ($P_{80} = 623{,}04$ pontos), gerando a flag binária `fl_alto_desempenho`.
- **Justificativa:** Um corte absoluto arbitrário (ex.: $\ge 650$ pontos) varia dependendo da dificuldade e calibração anual da TRI. O percentil 80 estabelece uma definição estável e balanceada (20% classe positiva vs. 80% classe negativa), permitindo avaliação fidedigna por PR-AUC e ROC-AUC sem inflação artificial por desbalanceamento severo.
- **Impacto:** O modelo de classificação atinge ROC-AUC de $0{,}804$ e PR-AUC de $0{,}535$ (contra baseline aleatório de $0{,}200$).

---

### ADR-08: Blindagem Metodológica contra Vazamento de Dados (*Anti-Data Leakage*)
- **Contexto:** O objetivo de negócio é prever o desempenho do candidato a partir do seu perfil socioeducacional prévio à realização do exame.
- **Decisão:**
  1. A matriz de features ($X$) é composta **exclusivamente por variáveis pré-prova** (renda familiar, tipo de escola, acesso à internet, raça, sexo, idade e localização geográfica).
  2. Todas as notas parciais (`NU_NOTA_*`) e indicadores de presença/ausência pós-prova são terminantemente excluídos de $X$.
  3. A divisão Treino/Teste (80% / 20%) é realizada antes de qualquer transformação, e os encoders/transformadores são ajustados (`fit`) **estritamente sobre o conjunto de treino**.
- **Justificativa:** Previne estimativas superotimistas e garante que os modelos sejam utilizáveis no mundo real para simulações ex-ante (como no aplicativo Streamlit da Sprint 6).

---

### ADR-09: Arquitetura de Modelagem em Larga Escala via `HistGradientBoosting`
- **Contexto:** O conjunto de treino contém mais de 2,14 milhões de registros com variáveis categóricas de alta cardinalidade (27 UFs, 17 classes de renda). Algoritmos tradicionais como `RandomForestClassifier` exigem dezenas de gigabytes de RAM e horas de processamento.
- **Decisão:** Utilizar `HistGradientBoostingRegressor` e `HistGradientBoostingClassifier` encapsulados em `Pipeline` com `ColumnTransformer`.
- **Justificativa:** O algoritmo agrupa features contínuas em até 256 bins de histogramas inteiros, permitindo treinamento completo em **menos de 35 segundos** com uso modesto de memória RAM (< 1 GB) e superando consistentemente os baselines lineares (Ridge $R^2 = 0{,}258 \to$ HistGB $R^2 = 0{,}295$; Regressão Logística ROC-AUC $0{,}790 \to$ HistGB ROC-AUC $0{,}804$).

---

### ADR-10: Explicabilidade Global e Amostragem Representativa para SHAP Values
- **Contexto:** O cálculo de valores Shapley (`shap.TreeExplainer`) possui complexidade computacional proporcional ao tamanho do conjunto de avaliação ($N = 535.653$).
- **Decisão:** Calcular os valores SHAP sobre uma **amostra estatisticamente representativa de $N = 5.000$ participantes** do conjunto de teste (com semente fixa `random_state=42`).
- **Justificativa:** Para um universo de 535 mil candidatos, uma amostra aleatória de 5.000 instâncias atinge margem de erro inferior a $1{,}4\%$ com $95\%$ de nível de confiança, reduzindo o tempo de cálculo de mais de 30 minutos para apenas **3,6 segundos**, viabilizando os gráficos Beeswarm e Bar Plot de impacto médio com total confiabilidade estatística.

