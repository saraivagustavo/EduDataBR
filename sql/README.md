# 🐘 Módulo SQL & Modelagem Relacional — EduDataBR

Bem-vindo ao módulo de Engenharia e Análise SQL do projeto **EduDataBR**.

Este diretório contém todos os artefatos relacionais desenvolvidos para o **PostgreSQL 17/18**, cobrindo desde a definição de esquemas (DDL) e ingestão de dados em lote (DML) até a criação de índices de alta performance, views analíticas e consultas avançadas com CTEs e Window Functions.

---

## 📂 Estrutura do Diretório

```text
sql/
├── 00_clean_csv.ipynb                    # Notebook de extração e redução dos microdados (ETL)
├── 01_create_database.sql                # Criação do banco de dados edudatabr
├── 02_create_table_enem.sql              # DDL da tabela enem_microdados com constraints e PK
├── 03_load_data.sql                      # Script de carga rápida via COPY / \copy
├── 04_create_indexes.sql                 # Índices B-Tree e índices parciais analíticos
│
├── views/                                # Camada semântica de Views Analíticas
│   ├── 01_vw_enem_presentes.sql          # View filtrada de participantes presentes com nota média
│   ├── 02_vw_resumo_por_uf.sql           # View agregada por estado (participação, evasão e notas)
│   └── 03_vw_desempenho_socioeconomico.sql # View cruzando renda familiar e inclusão digital
│
└── queries/                              # Consultas Analíticas (Respondendo às Perguntas de Negócio)
    ├── 01_visao_geral.sql                # Contagem total de inscritos vs participantes presentes
    ├── 02_notas_por_estados.sql          # Médias de desempenho por Unidade da Federação
    ├── 03_escola_publica_privada.sql     # Comparativo geral entre escola pública e privada
    ├── 04_desempenho_por_renda.sql       # Médias de notas pelas 17 faixas de renda familiar (PQ1)
    ├── 05_desempenho_acesso_internet.sql # Desempenho geral por acesso à internet
    ├── 06_ranking_estados_window_functions.sql # Ranking com RANK(), NTILE(4) e médias nacionais (PQ5)
    ├── 07_impacto_internet_controlado_renda.sql # Ganho da internet fatiado por classe salarial (PQ2)
    ├── 08_gap_escola_publica_privada_por_renda.sql # Vantagem da escola privada controlada por renda (PQ4)
    ├── 09_disparidade_genero_por_disciplina.sql # Comparativo de gênero nas 5 áreas do conhecimento (PQ6)
    └── 10_evasao_segundo_dia_socioeconomico.sql # Taxa de abandono do 2º domingo por renda e internet (PQ8)
```

---

## ⚙️ Guia de Execução Passo a Passo

Os scripts foram desenhados para serem executados em ordem sequencial no **pgAdmin 4**, **DBeaver** ou via terminal **`psql`**:

### Passo 1: Criar o Banco de Dados
Conecte-se ao seu servidor PostgreSQL e execute:
```sql
-- Arquivo: sql/01_create_database.sql
CREATE DATABASE edudatabr;
```

### Passo 2: Conectar ao banco `edudatabr` e Criar a Tabela
Conectado ao banco `edudatabr`, execute o DDL refinado:
```sql
-- Arquivo: sql/02_create_table_enem.sql
\i sql/02_create_table_enem.sql
```

### Passo 3: Importar os Microdados (~3,93M de registros)
Você pode executar o script [`03_load_data.sql`](03_load_data.sql) diretamente no Query Tool:
```sql
COPY enem_microdados
FROM 'C:/Users/User/Desktop/edudatabr/data/interim/microdados_enem_2023_reduzido.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';
```
*Dica para execução via terminal cliente `psql` (caso o servidor não tenha permissão de leitura direta no disco do usuário):*
```sql
\copy enem_microdados FROM 'C:/Users/User/Desktop/edudatabr/data/interim/microdados_enem_2023_reduzido.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
```

### Passo 4: Criar os Índices de Performance
```sql
-- Arquivo: sql/04_create_indexes.sql
\i sql/04_create_indexes.sql
```
*Destaque de Engenharia:* Além dos índices B-Tree tradicionais em `sg_uf_prova`, `tp_escola` e `q006`, foi implementado um **Índice Parcial** (`idx_enem_presentes_analitico`) que indexa exclusivamente os ~2,69 milhões de candidatos presentes, reduzindo drasticamente o tempo de varredura das queries analíticas.

### Passo 5: Criar as Views Analíticas
Execute os scripts da pasta `sql/views/` para disponibilizar a camada semântica simplificada.

### Passo 6: Executar as Consultas Analíticas
Execute qualquer script da pasta `sql/queries/` para extrair os insights e responder às perguntas de negócio do projeto.

---

## 🎯 Rastreabilidade das Consultas com as Perguntas de Negócio

| Script | Pergunta de Negócio | Técnicas Utilizadas |
|---|---|---|
| `04_desempenho_por_renda.sql` | **PQ1** (Gradiente de Renda) | Agregações `GROUP BY` e `ROUND(AVG())` |
| `07_impacto_internet_controlado_renda.sql` | **PQ2** (Isolamento da Internet) | CTEs, `FILTER(WHERE...)` e ganho absoluto/relativo |
| `03_escola_publica_privada.sql` | **PQ3** (Gap Pública x Privada) | `CASE WHEN` categórico e agrupamentos |
| `08_gap_escola_publica_privada_por_renda.sql` | **PQ4** (Mediação do Gap Escolar por Renda) | CTEs e agregações cruzadas |
| `06_ranking_estados_window_functions.sql` | **PQ5** (Assimetrias Regionais) | Window Functions (`RANK()`, `NTILE(4)`, `AVG() OVER()`) |
| `09_disparidade_genero_por_disciplina.sql` | **PQ6** (Disparidades de Gênero) | CTEs e cálculo de gap por domínio |
| `10_evasao_segundo_dia_socioeconomico.sql` | **PQ8** (Evasão do 2º Domingo) | `FILTER`, taxas de conversão e evasão |
