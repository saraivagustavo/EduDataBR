# EduDataBR

**Análise de dados educacionais e predição de desempenho no ENEM**

O EduDataBR é um projeto acadêmico de análise, engenharia e ciência de dados aplicado aos microdados oficiais do Exame Nacional do Ensino Médio (ENEM), disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A proposta central é investigar fatores associados ao desempenho dos participantes, com atenção especial a desigualdades educacionais, socioeconômicas e regionais. O projeto contempla desde a organização dos dados brutos até análises exploratórias, consultas SQL, modelagem preditiva e construção de visualizações interativas.

---

## Visão Geral

O projeto busca integrar práticas de análise de dados e pesquisa aplicada em educação, compondo um fluxo completo de trabalho:

- Ingestão e organização dos microdados do ENEM;
- Limpeza, padronização e preparação dos dados;
- Análise exploratória de variáveis educacionais e socioeconômicas;
- Consultas SQL para extração de indicadores;
- Engenharia de atributos para modelagem;
- Desenvolvimento de modelos preditivos;
- Visualização dos resultados em relatórios e dashboard interativo.

---

## Objetivos

### Objetivo Geral

Analisar os microdados do ENEM com o propósito de identificar padrões, desigualdades e fatores associados ao desempenho dos candidatos brasileiros.

### Objetivos Específicos

- Tratar e estruturar os dados do ENEM para análise;
- Investigar diferenças de desempenho por estado, região e tipo de escola;
- Avaliar relações entre renda familiar, acesso à internet e notas;
- Produzir consultas SQL para geração de indicadores educacionais;
- Construir visualizações estatísticas para apoio à interpretação dos dados;
- Desenvolver modelos de Machine Learning para previsão ou classificação de desempenho;
- Disponibilizar resultados por meio de relatórios e dashboard interativo.

---

## Fonte de Dados

Os dados utilizados no projeto são provenientes dos microdados oficiais do ENEM, publicados pelo:

**Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)**  
Portal: [https://www.gov.br/inep](https://www.gov.br/inep)

> Observação: os microdados do ENEM possuem grande volume e, por boas práticas de versionamento, não devem ser armazenados diretamente no repositório.

---

## Estrutura do Projeto

```text
edudatabr/
├── app/                  # Aplicação e dashboard interativo
├── data/                 # Diretório local para dados brutos e tratados
├── docs/                 # Documentação e planejamento do projeto
├── notebooks/            # Notebooks de exploração, limpeza e análise
├── reports/              # Relatórios analíticos e resultados consolidados
├── sql/                  # Scripts SQL de criação, carga e consultas
│   └── queries/          # Consultas analíticas
├── src/                  # Código-fonte modular do projeto
├── tests/                # Testes automatizados
├── main.py               # Ponto de entrada do projeto
├── requirements.txt      # Dependências Python
└── README.md             # Documentação principal
```

---

## Consultas SQL

O diretório `sql/queries` reúne consultas voltadas à extração de indicadores educacionais:

| Arquivo | Descrição |
| --- | --- |
| `01_visao_geral.sql` | Visão geral da base e métricas iniciais |
| `02_notas_por_estados.sql` | Desempenho médio por unidade federativa |
| `03_escola_publica_privada.sql` | Comparação entre escolas públicas e privadas |
| `04_desempenho_por_renda.sql` | Relação entre renda familiar e desempenho |
| `05_desempenho_acesso_internet.sql` | Associação entre acesso à internet e notas |

---

## Tecnologias

### Linguagem e Ambiente

- Python
- SQL
- Jupyter Notebook

### Bibliotecas de Análise e Visualização

- Pandas
- NumPy
- Matplotlib
- Seaborn

### Modelagem Preditiva

- Scikit-learn
- XGBoost

### Aplicação e Versionamento

- Streamlit
- Git e GitHub
- VS Code

---

## Possíveis Análises

O projeto prevê análises voltadas à compreensão de desigualdades e padrões de desempenho no ENEM, incluindo:

- Distribuição das notas por área do conhecimento;
- Desempenho médio por estado e região;
- Comparação entre estudantes de escolas públicas e privadas;
- Relação entre renda familiar e desempenho;
- Impacto do acesso à internet no resultado dos participantes;
- Correlação entre variáveis socioeconômicas e notas;
- Identificação de grupos com maior vulnerabilidade educacional.

---

## Modelagem Preditiva

A etapa de modelagem poderá incluir modelos supervisionados para:

- Prever a nota média dos candidatos;
- Classificar faixas de desempenho;
- Identificar variáveis com maior influência sobre os resultados;
- Comparar diferentes algoritmos de regressão e classificação.

Métricas previstas para avaliação:

- MAE;
- RMSE;
- R²;
- Accuracy;
- F1-score.

---

## Roadmap

| Etapa | Descrição | Status |
| --- | --- | --- |
| 1 | Estruturação do projeto e ambiente | Em andamento |
| 2 | Obtenção e organização dos microdados | Planejado |
| 3 | Limpeza e tratamento dos dados | Planejado |
| 4 | Análise exploratória dos dados | Planejado |
| 5 | Consultas SQL e indicadores | Em andamento |
| 6 | Engenharia de atributos | Planejado |
| 7 | Modelagem preditiva | Planejado |
| 8 | Dashboard e relatório final | Planejado |

---

## Como Executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd edudatabr
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os notebooks ou a aplicação Streamlit conforme a etapa do projeto:

```bash
streamlit run app/streamlit_app.py
```

---

## Status do Projeto

**Em desenvolvimento.**

O projeto está em fase de estruturação, exploração inicial dos dados e construção das primeiras consultas analíticas.

---

## Autor e Contato

**Gustavo Saraiva**
<p align="center">
  <a href="https://www.linkedin.com/in/gustavo-saraiva-mariano/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/saraivagustavo"><img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.instagram.com/saraivag10/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
</p>

