<div align="center">

# EduDataBR

### Data Engineering • Data Analytics • Data Science

Projeto de análise de dados educacionais utilizando os microdados oficiais do ENEM para investigar fatores que influenciam o desempenho dos estudantes brasileiros.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.5-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-17-4169E1?logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-1.7-F7931E?logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Status-In_Development-yellow">
</p>

</div>

---

## 📑 Sumário

<details>
<summary><strong>📌 1. Sobre o Projeto</strong></summary>

- [Visão Geral](#-visão-geral)
- [Contexto](#-contexto)
- [Objetivos](#-objetivos)
  - [Objetivo Geral](#objetivo-geral)
  - [Objetivos Específicos](#objetivos-específicos)
- [Arquitetura do Projeto](#-arquitetura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)

</details>

<details>
<summary><strong>⚙️ 2. Engenharia & Desenvolvimento</strong></summary>

- [Estrutura do Repositório](#-estrutura-do-repositório)
  - [Navegação do Projeto](#-navegação-do-projeto)
- [Documentação Técnica](#-documentação-técnica)
- [Escopo do Projeto](#-escopo-do-projeto)
  - [O que o projeto contempla](#o-projeto-contempla)
  - [O que o projeto não contempla](#o-projeto-nao-contempla)
- [Metodologia](#-metodologia)
- [Roadmap](#-roadmap)
- [Status Atual](#-status-atual)
- [Como Executar o Projeto](#-como-executar-o-projeto)

</details>

<details>
<summary><strong>🤝 3. Colaboração & Contribuição</strong></summary>

- [Contribuições](#-contribuições)

</details>

<details>
<summary><strong>👨‍💻 4. Informações do Projeto</strong></summary>

- [Autor](#-autor)
- [Licença](#-licença)

</details>

---

# 📖 Visão Geral

O **EduDataBR** é um projeto de Engenharia de Dados, Análise de Dados e Ciência de Dados desenvolvido a partir dos microdados oficiais do Exame Nacional do Ensino Médio (ENEM), disponibilizados anualmente pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

O projeto tem como propósito construir uma solução completa para análise de dados educacionais, contemplando todas as etapas do ciclo de vida dos dados: obtenção, preparação, armazenamento, análise, modelagem e visualização.

Utilizando uma das maiores bases públicas de dados do Brasil, o EduDataBR busca investigar fatores socioeconômicos, demográficos e educacionais que podem estar relacionados ao desempenho dos participantes no ENEM. Além da geração de insights, o projeto também pretende reproduzir um fluxo de trabalho semelhante ao adotado em equipes profissionais de dados, aplicando boas práticas de Engenharia de Dados, SQL Analítico, Análise Exploratória de Dados (EDA), Ciência de Dados e Machine Learning.

Todo o desenvolvimento é guiado por uma metodologia estruturada, com documentação técnica, registro das decisões tomadas e foco na reprodutibilidade, permitindo que o projeto evolua de forma organizada e transparente.

---

# 🌎 Contexto

O Exame Nacional do Ensino Médio (ENEM) é atualmente a principal forma de acesso ao ensino superior brasileiro, sendo utilizado como critério de seleção em programas como o Sistema de Seleção Unificada (SISU), o Programa Universidade para Todos (ProUni) e o Fundo de Financiamento Estudantil (FIES), além de diversas instituições públicas e privadas.

Anualmente, o Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) disponibiliza os **Microdados do ENEM**, uma base pública composta por milhões de registros e centenas de variáveis relacionadas ao perfil dos participantes, características socioeconômicas, informações sobre a trajetória escolar e desempenho nas provas.

Embora esses dados estejam disponíveis para toda a sociedade, seu volume e complexidade tornam sua exploração um desafio. Nesse contexto, o EduDataBR propõe a construção de um ambiente estruturado para transformar esses dados em informações úteis, permitindo identificar padrões, levantar hipóteses e produzir evidências que contribuam para a compreensão de fatores associados ao desempenho dos estudantes brasileiros.

---

# 🎯 Objetivos

## Objetivo Geral

Desenvolver uma solução completa de Engenharia e Análise de Dados utilizando os microdados oficiais do ENEM, com o objetivo de investigar fatores associados ao desempenho dos estudantes brasileiros e demonstrar a aplicação de boas práticas em projetos de dados, desde a ingestão e preparação das informações até a geração de análises, modelos preditivos e visualizações interativas.

## Objetivos Específicos

- Estruturar um pipeline de dados organizado e reproduzível para processamento dos microdados do ENEM.
- Realizar o entendimento e a documentação das variáveis presentes na base de dados.
- Avaliar a qualidade dos dados, identificando inconsistências, valores ausentes e oportunidades de tratamento.
- Desenvolver consultas analíticas em SQL para responder perguntas de negócio relacionadas ao desempenho dos participantes.
- Realizar Análise Exploratória de Dados (EDA) para identificar padrões, tendências e possíveis relações entre variáveis.
- Construir novas variáveis (Feature Engineering) que agreguem valor às análises e aos modelos preditivos.
- Desenvolver modelos de Machine Learning para investigar a capacidade preditiva dos dados socioeconômicos e educacionais.
- Construir um dashboard interativo para facilitar a exploração dos resultados obtidos.
- Documentar todas as etapas do projeto, registrando decisões técnicas, metodologia utilizada e principais descobertas.

---

# 🏗️ Arquitetura do Projeto

O EduDataBR foi concebido como um pipeline completo de dados, reproduzindo as principais etapas encontradas em projetos de Engenharia de Dados, Análise de Dados e Ciência de Dados.

Cada componente possui uma responsabilidade específica dentro do fluxo, garantindo organização, reprodutibilidade e facilidade de manutenção.

```text
                    Microdados ENEM (INEP)
                              │
                              ▼
                    Coleta e Organização
                         (Data Lake)
                              │
                              ▼
                  Preparação e Limpeza (ETL)
                           Python
                              │
                              ▼
                 Armazenamento Estruturado
                         PostgreSQL
                              │
                              ▼
                    Consultas Analíticas
                             SQL
                              │
                              ▼
                 Análise Exploratória de Dados
                       Jupyter Notebook
                              │
                              ▼
                  Engenharia de Features
                              │
                              ▼
                    Machine Learning
                              │
                              ▼
                  Dashboards e Relatórios
```

---

# 🛠️ Tecnologias Utilizadas

O EduDataBR integra ferramentas amplamente utilizadas em projetos de Engenharia de Dados, Análise de Dados e Ciência de Dados. Cada tecnologia foi selecionada para desempenhar uma função específica dentro da arquitetura do projeto.

| Tecnologia | Função no Projeto |
|------------|-------------------|
| **Python** | Linguagem principal utilizada para desenvolvimento do pipeline de dados, ETL, análises, modelagem e automação. |
| **PostgreSQL** | Armazenamento estruturado dos dados e execução de consultas analíticas em SQL. |
| **Pandas** | Manipulação, limpeza e transformação dos conjuntos de dados. |
| **Scikit-Learn** | Desenvolvimento e avaliação dos modelos de Machine Learning. |
| **Jupyter Notebook** | Ambiente para Análise Exploratória de Dados (EDA), experimentação e documentação das análises. |
| **Git & GitHub** | Controle de versão, documentação e gerenciamento do projeto. |

---

# 📂 Estrutura do Repositório

O EduDataBR foi organizado em módulos independentes, refletindo as diferentes etapas do ciclo de vida dos dados. Cada diretório possui uma responsabilidade específica dentro da arquitetura do projeto, promovendo organização, reprodutibilidade e facilidade de manutenção.

Além da separação entre dados, código-fonte, documentação e resultados, cada módulo conta com um **README próprio**, detalhando sua finalidade, estrutura interna e papel dentro do projeto.

```text
EduDataBR/
│
├── app/                    # Aplicação para visualização dos resultados
├── data/                   # Dados utilizados no projeto
│   ├── raw/                # Dados originais obtidos do INEP
│   ├── interim/            # Dados intermediários após o ETL
│   └── processed/          # Dados prontos para análises
│
├── docs/                   # Documentação técnica
├── notebooks/              # Estudos, EDA e experimentos
├── reports/                # Relatórios, gráficos e resultados
├── sql/                    # Scripts SQL
├── src/                    # Código-fonte
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 📁 Navegação do Projeto

Cada diretório do repositório possui uma documentação própria, permitindo compreender rapidamente sua organização e responsabilidade dentro da arquitetura do EduDataBR.

| Diretório | Descrição |
|-----------|-----------|
| 📁 [`app/`](app/) | Aplicação responsável pela visualização dos resultados, dashboards e futuras interfaces do projeto. |
| 📁 [`data/`](data/) | Organização dos dados em seus diferentes estágios: brutos, intermediários e processados. |
| 📁 [`docs/`](docs/) | Documentação técnica, metodologia, decisões de projeto e materiais de apoio. |
| 📁 [`notebooks/`](notebooks/) | Análises exploratórias, experimentos, validações e estudos realizados durante o desenvolvimento. |
| 📁 [`reports/`](reports/) | Relatórios, gráficos, figuras e demais artefatos produzidos pelo projeto. |
| 📁 [`sql/`](sql/) | Scripts SQL utilizados para criação do banco de dados, consultas analíticas, views e demais objetos relacionais. |
| 📁 [`src/`](src/) | Código-fonte do projeto, incluindo pipeline ETL, engenharia de atributos, modelos e utilitários. |

> **Cada diretório possui um README específico**, contendo informações detalhadas sobre sua organização, convenções e responsabilidades.

---

## 📚 Documentação Técnica

Além da documentação presente em cada diretório, o EduDataBR possui uma documentação técnica dedicada, organizada para registrar todas as etapas do desenvolvimento do projeto.

| Documento | Descrição |
|-----------|-----------|
| 📖 [`README`](docs/README.md) | Índice da documentação técnica. |
| 📄 [`01 - Entendimento do Negócio`](docs/01_business_understanding.md) | Contexto, motivação, escopo e objetivos do projeto. |
| 📄 [`02 - Dicionário de Dados`](docs/02_data_dictionary.md) | Descrição das variáveis selecionadas dos microdados do ENEM. |
| 📄 [`03 - Qualidade dos Dados`](docs/03_data_quality.md) | Avaliação da qualidade dos dados e decisões de tratamento. |
| 📄 [`04 - Perguntas de Negócio`](docs/04_business_questions.md) | Questões que direcionam as análises do projeto. |
| 📄 [`05 - Hipóteses`](docs/05_hypotheses.md) | Hipóteses formuladas antes das análises. |
| 📄 [`06 - Decisões Técnicas`](docs/06_decisions.md) | Registro das principais decisões técnicas tomadas durante o desenvolvimento. |
| 📄 [`07 - Metodologia`](docs/07_methodology.md) | Processo de desenvolvimento adotado pelo projeto. |
| 📄 [`08 - Roadmap`](docs/08_roadmap.md) | Planejamento, evolução e próximos passos do EduDataBR. |

---

## 🚀 Continue Explorando

Este README apresenta uma visão geral do EduDataBR.

Para conhecer em detalhes a metodologia adotada, as decisões técnicas, a documentação das variáveis e a evolução do projeto, acesse a documentação técnica:

➡️ **[`Ir para a Documentação Técnica`](docs/README.md)**

Você também pode navegar diretamente pelos módulos do repositório utilizando os links disponíveis na seção **Navegação do Projeto**.

---

# 🎯 Escopo do Projeto

O EduDataBR foi concebido como um projeto de portfólio técnico com foco na aplicação de conceitos de Engenharia de Dados, Análise de Dados e Ciência de Dados utilizando uma base pública de grande escala. O objetivo não é esgotar todas as possibilidades de análise dos microdados do ENEM, mas construir uma solução completa, organizada e reproduzível que demonstre boas práticas ao longo de todo o ciclo de vida dos dados.

## O projeto contempla

- ✅ Ingestão e organização dos microdados oficiais do ENEM.
- ✅ Processo de ETL para preparação e transformação dos dados.
- ✅ Modelagem e armazenamento em banco de dados relacional (PostgreSQL).
- ✅ Consultas analíticas utilizando SQL.
- ✅ Análise Exploratória de Dados (EDA).
- ✅ Engenharia de atributos (Feature Engineering).
- ✅ Desenvolvimento de modelos de Machine Learning.
- ✅ Construção de dashboards para visualização dos resultados.
- ✅ Documentação técnica de todas as etapas do projeto.

## O projeto não contempla

- ❌ Inferências causais sobre os fatores que influenciam o desempenho dos estudantes.
- ❌ Utilização de dados privados ou informações pessoais dos participantes.
- ❌ Processamento distribuído (Big Data) ou streaming de dados.
- ❌ Desenvolvimento de modelos para uso em ambientes de produção.
- ❌ Avaliações ou recomendações educacionais individuais.

---

# 🧭 Metodologia

O desenvolvimento do EduDataBR segue uma abordagem inspirada no **CRISP-DM (Cross Industry Standard Process for Data Mining)**, adaptada para contemplar práticas modernas de Engenharia de Dados e Análise de Dados.

Cada etapa do projeto possui objetivos bem definidos, documentação própria e critérios de conclusão, permitindo que o desenvolvimento seja incremental, organizado e reproduzível.

```text
Entendimento do Negócio
        │
        ▼
Entendimento dos Dados
        │
        ▼
Avaliação da Qualidade dos Dados
        │
        ▼
SQL Analytics
        │
        ▼
Análise Exploratória de Dados
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning
        │
        ▼
Dashboards e Storytelling
```

Ao longo do projeto, todas as decisões técnicas, hipóteses, resultados e aprendizados são registrados na documentação técnica disponível na pasta [`docs/`](docs/).

---

# 🗺️ Roadmap

## Sprint 1 — Estruturação do Projeto

- [x] Definição da arquitetura do repositório.
- [x] Configuração do ambiente de desenvolvimento.
- [x] Organização dos microdados.
- [x] Configuração do PostgreSQL.
- [x] Estrutura inicial da documentação.

---

## Sprint 2 — Data Understanding

- [ ] Estudo do dicionário dos microdados.
- [ ] Seleção das variáveis relevantes.
- [ ] Construção do Data Dictionary.
- [ ] Avaliação da qualidade dos dados.

---

## Sprint 3 — SQL Analytics

- [ ] Criação do banco de dados definitivo.
- [ ] Desenvolvimento de consultas analíticas.
- [ ] Construção de Views.
- [ ] Utilização de CTEs.
- [ ] Geração dos primeiros insights.

---

## Sprint 4 — Exploratory Data Analysis

- [ ] Estatísticas descritivas.
- [ ] Distribuições.
- [ ] Correlações.
- [ ] Visualizações.

---

## Sprint 5 — Machine Learning

- [ ] Preparação dos dados.
- [ ] Engenharia de atributos.
- [ ] Treinamento dos modelos.
- [ ] Avaliação dos resultados.

---

## Sprint 6 — Dashboard

- [ ] Desenvolvimento da aplicação.
- [ ] Visualizações interativas.
- [ ] Storytelling dos resultados.
- [ ] Publicação do projeto.

---

# 📈 Status Atual

| Item | Situação |
|------|----------|
| **Fase Atual** | Data Understanding |
| **Etapa em Desenvolvimento** | Construção do Data Dictionary |
| **Última Atualização** | Julho de 2026 |
| **Status Geral** | 🟡 Em desenvolvimento |

### Próximos Passos

- Documentar as variáveis selecionadas dos microdados.
- Avaliar a qualidade da base de dados.
- Definir as primeiras perguntas de negócio.
- Iniciar as consultas analíticas em SQL.

---

# 🚀 Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone https://github.com/saraivagustavo/EduDataBR.git
```

## 2. Acesse o diretório do projeto

```bash
cd EduDataBR
```

## 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

## 4. Ative o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

## 6. Configure o banco de dados

Crie um banco de dados PostgreSQL e importe os microdados processados seguindo as instruções disponíveis na documentação da pasta [`sql/`](sql/).

## 7. Execute os notebooks

Após configurar o ambiente e o banco de dados, os notebooks podem ser executados normalmente através do Jupyter Notebook ou Visual Studio Code.

---

# 🤝 Contribuições

Contribuições são sempre bem-vindas.

Caso identifique alguma melhoria, erro ou oportunidade de evolução, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

Toda sugestão será analisada e, quando alinhada aos objetivos do projeto, poderá ser incorporada às próximas versões.

---

# 👨‍💻 Autor

<table>
<tr>

<td width="170">

<img src="https://github.com/saraivagustavo.png" width="150">

</td>

<td>

### Gustavo Saraiva Mariano

Graduando em Sistemas de Informação pelo Instituto Federal do Espírito Santo (IFES).

Interessado em:

- Engenharia de Dados
- Análise de Dados
- Ciência de Dados
- Machine Learning
- Desenvolvimento em Python

**GitHub**

https://github.com/saraivagustavo

**LinkedIn**

https://www.linkedin.com/in/gustavo-saraiva/

</td>

</tr>
</table>

---

# 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.

Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.