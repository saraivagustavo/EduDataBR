# Planejamento do Projeto — EduDataBR

# 🎯 Objetivo Principal

Desenvolver um projeto completo de análise de dados utilizando os microdados do ENEM, aplicando conceitos de:

- análise de dados
- engenharia de dados
- ciência de dados
- visualização de dados
- machine learning

---

# 📅 Roadmap do Projeto

## Etapa 1 — Estruturação do Projeto
### Objetivos
- Criar estrutura de pastas
- Configurar ambiente Python
- Inicializar repositório Git
- Organizar documentação inicial

### Status
✅ Em andamento

---

## Etapa 2 — Obtenção dos Dados
### Objetivos
- Baixar microdados do ENEM
- Analisar dicionário de dados
- Identificar variáveis relevantes

### Entregáveis
- Dataset bruto salvo em `data/raw`
- Documento com descrição das colunas

---

## Etapa 3 — Limpeza e Tratamento
### Objetivos
- Remover inconsistências
- Tratar valores ausentes
- Filtrar participantes válidos
- Padronizar variáveis

### Entregáveis
- Dataset limpo
- Scripts de processamento

---

## Etapa 4 — Análise Exploratória (EDA)
### Objetivos
- Identificar padrões
- Criar visualizações
- Levantar hipóteses

### Possíveis análises
- Média de notas por estado
- Relação entre renda e desempenho
- Comparação escola pública x privada
- Distribuição das notas

### Entregáveis
- Notebook EDA
- Gráficos e insights

---

## Etapa 5 — Engenharia de Features
### Objetivos
- Criar novas variáveis
- Construir indicadores
- Preparar dados para modelagem

### Possíveis features
- Média geral
- Indicador socioeconômico
- Classificação de desempenho
- Indicador de acesso à tecnologia

---

## Etapa 6 — Modelagem Preditiva
### Objetivos
- Treinar modelos de Machine Learning
- Avaliar desempenho
- Comparar algoritmos

### Modelos previstos
- Regressão Linear
- Random Forest
- XGBoost

### Métricas
- RMSE
- MAE
- R²
- Accuracy
- F1-score

---

## Etapa 7 — Dashboard Interativo
### Objetivos
- Desenvolver interface visual
- Permitir filtros interativos
- Exibir insights do projeto

### Ferramentas
- Streamlit
- Power BI (opcional)

---

## Etapa 8 — Finalização e Deploy
### Objetivos
- Organizar repositório
- Melhorar README
- Publicar aplicação
- Revisar documentação

### Possíveis plataformas
- Streamlit Cloud
- Render
- GitHub Pages

---

# 🛠️ Stack Tecnológica

## Backend / Dados
- Python
- Pandas
- NumPy

## Visualização
- Matplotlib
- Seaborn
- Plotly

## Machine Learning
- Scikit-learn
- XGBoost

## Dashboard
- Streamlit

## Versionamento
- Git/GitHub

---

# 📂 Organização dos Dados

## Raw
Dados brutos originais do ENEM.

## Interim
Dados parcialmente tratados.

## Processed
Dados finais preparados para análise/modelagem.

---

# 📌 Observações

- O projeto terá foco acadêmico e profissional.
- O código será modularizado visando boas práticas.
- Todo o pipeline será documentado.
- O projeto será desenvolvido de forma incremental.
- Feedbacks serão bem-vindos para melhorias contínuas.