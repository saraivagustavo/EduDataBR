# 📖 Dicionário de Dados — EduDataBR

## 1. Objetivo

Este documento apresenta o dicionário de dados utilizado pelo EduDataBR, descrevendo as variáveis selecionadas para as análises e documentando suas características, significados e tratamentos realizados ao longo do projeto.

O objetivo é estabelecer uma referência única para compreensão dos dados utilizados nas etapas de Engenharia de Dados, Análise de Dados e Ciência de Dados.

---

# 2. Fonte dos Dados

## 2.1 Fonte principal

**Instituição:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)  
**Dataset:** Microdados do Exame Nacional do Ensino Médio (ENEM)  
**Ano:** 2023  
**Tipo:** Dados públicos  

> As informações apresentadas neste documento são confrontadas e validadas com base na documentação oficial disponibilizada pelo INEP (`Dicionário_Microdados_Enem_2023.xlsx` e scripts de input oficiais).

---

# 3. Organização do Dicionário

As variáveis são documentadas de acordo com sua função analítica dentro do projeto:

- **Identificação**: Chaves de registro e controle temporal;
- **Características demográficas e geográficas**: Perfil do candidato e localização da prova;
- **Características socioeconômicas**: Renda familiar e acesso a recursos digitais;
- **Características educacionais**: Trajetória e dependência escolar;
- **Participação no exame**: Presença e abstenção por dia de aplicação;
- **Desempenho**: Notas obtidas nas 4 áreas de conhecimento e na redação.

---

# 4. Convenções

| Campo | Descrição |
|---|---|
| **Variável** | Nome original da coluna presente na base do INEP. |
| **Tipo** | Tipo de dado adotado no projeto / PostgreSQL. |
| **Descrição** | Significado da variável segundo a documentação oficial. |
| **Domínio** | Valores, categorias ou intervalo permitidos. |
| **Nulos** | Presença e volume de valores ausentes observados. |
| **Tratamento** | Regras de limpeza, filtragem ou imputação aplicadas. |
| **Utilização** | Finalidade analítica e modelagem. |
| **Observações** | Particularidades contextuais relevantes. |

---

# 5. Variáveis do Projeto

## 5.1 Identificação

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---:|---|---|---|
| `nu_inscricao` | `TEXT` / `BIGINT` | Número de inscrição do participante no ENEM. | Numérico único | 0 | Chave primária de identificação | Identificação unívoca do registro | Armazenado como texto ou inteiro de 64 bits para evitar perda de precisão. |
| `nu_ano` | `INTEGER` | Ano de realização do exame. | `2023` | 0 | Manter constante | Filtro temporal e particionamento | Representa a edição avaliada do exame (2023). |

---

## 5.2 Características Demográficas e Geográficas

As informações demográficas seguem a política de privacidade e anonimização do INEP (ex.: faixas etárias agrupadas).

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---:|---|---|---|
| `tp_faixa_etaria` | `INTEGER` | Faixa etária codificada do participante. | `1` a `20` | 0 | Categorização | Análise demográfica de idade | `1` = Menor de 17 anos; `2` = 17 anos; `3` = 18 anos ... até `20` = Maior de 70 anos. |
| `tp_sexo` | `CHAR(1)` | Sexo declarado do participante. | `M`, `F` | 0 | Manter original | Comparação demográfica | `M` = Masculino; `F` = Feminino. |
| `tp_cor_raca` | `INTEGER` | Cor ou raça autodeclarada. | `0` a `5` | 0 | Manter original | Equidade racial e desempenho | `0` = Não declarado; `1` = Branca; `2` = Preta; `3` = Parda; `4` = Amarela; `5` = Indígena. |
| `sg_uf_prova` | `CHAR(2)` | Sigla da Unidade da Federação onde a prova foi realizada. | 27 UFs | 0 | Padronização geográfica | Análise espacial e regional | Permite agrupamento por estados e pelas 5 macrorregiões brasileiras. |

---

## 5.3 Características Socioeconômicas

Variáveis extraídas do Questionário Socioeconômico do ENEM.

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---:|---|---|---|
| `q006` | `CHAR(1)` | Faixa de renda mensal familiar. | `A` a `Q` | 0 | Manter original / Agrupar classes | Análise de desigualdade econômica | 17 faixas salariais progressivas. |
| `q025` | `CHAR(1)` | Acesso à internet na residência do candidato. | `A`, `B` | 0 | Mapear para booleano | Inclusão digital e impacto na aprendizagem | `A` = Não possui; `B` = Possui. |

### 5.3.1 Distribuição da Renda Familiar (`q006`)
*Total analisado: 3.933.955 registros.*

| Código | Intervalo de Renda Familiar Mensal | Quantidade | Percentual |
|---|---|---:|---:|
| `A` | Nenhuma renda | 268.053 | 6,81% |
| `B` | Até R$ 1.320,00 (1 Salário Mínimo) | 1.245.271 | 31,65% |
| `C` | De R$ 1.320,01 até R$ 1.980,00 | 650.942 | 16,55% |
| `D` | De R$ 1.980,01 até R$ 2.640,00 | 437.366 | 11,12% |
| `E` | De R$ 2.640,01 até R$ 3.300,00 | 293.994 | 7,47% |
| `F` | De R$ 3.300,01 até R$ 3.960,00 | 171.344 | 4,36% |
| `G` | De R$ 3.960,01 até R$ 5.280,00 | 261.327 | 6,64% |
| `H` | De R$ 5.280,01 até R$ 6.600,00 | 139.279 | 3,54% |
| `I` | De R$ 6.600,01 até R$ 7.920,00 | 85.970 | 2,19% |
| `J` | De R$ 7.920,01 até R$ 9.240,00 | 75.179 | 1,91% |
| `K` | De R$ 9.240,01 até R$ 10.560,00 | 59.631 | 1,52% |
| `L` | De R$ 10.560,01 até R$ 11.880,00 | 39.596 | 1,01% |
| `M` | De R$ 11.880,01 até R$ 13.200,00 | 33.626 | 0,85% |
| `N` | De R$ 13.200,01 até R$ 15.840,00 | 41.565 | 1,06% |
| `O` | De R$ 15.840,01 até R$ 19.800,00 | 41.218 | 1,05% |
| `P` | De R$ 19.800,01 até R$ 26.400,00 | 38.105 | 0,97% |
| `Q` | Mais de R$ 26.400,00 | 51.489 | 1,31% |

### 5.3.2 Distribuição do Acesso à Internet (`q025`)
| Código | Acesso Domiciliar à Internet | Quantidade | Percentual |
|---|---|---:|---:|
| `A` | Não | 375.504 | 9,55% |
| `B` | Sim | 3.558.451 | 90,45% |

---

## 5.4 Características Educacionais

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---:|---|---|---|
| `tp_escola` | `INTEGER` | Tipo de escola do Ensino Médio do participante. | `1`, `2`, `3` | 0 | Categorização | Desempenho rede pública vs privada | `1` = Não respondeu; `2` = Pública; `3` = Privada. |

### 5.4.1 Distribuição da variável `tp_escola`
| Código | Categoria | Quantidade | Percentual |
|:---:|---|---:|---:|
| `1` | Não respondeu / Já concluído | 2.532.796 | 64,38% |
| `2` | Pública | 1.166.540 | 29,65% |
| `3` | Privada | 234.619 | 5,96% |

> **Nota técnica:** Participantes que já concluíram o Ensino Médio em anos anteriores ou não prestaram essa informação específica na inscrição constam com código `1`. Para comparações diretas de redes de ensino, filtram-se candidatos com códigos `2` e `3`.

---

## 5.5 Participação no Exame

O ENEM é aplicado em dois domingos consecutivos:
- **Dia 1**: Linguagens e Códigos (`LC`), Ciências Humanas (`CH`) e Redação;
- **Dia 2**: Ciências da Natureza (`CN`) e Matemática (`MT`).

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização |
|---|---|---|---|---:|---|---|
| `tp_presenca_cn` | `INTEGER` | Presença em Ciências da Natureza (Dia 2). | `0`, `1`, `2` | 0 | Filtro de público presente | `0` = Faltou; `1` = Presente; `2` = Eliminado. |
| `tp_presenca_ch` | `INTEGER` | Presença em Ciências Humanas (Dia 1). | `0`, `1`, `2` | 0 | Filtro de público presente | `0` = Faltou; `1` = Presente; `2` = Eliminado. |
| `tp_presenca_lc` | `INTEGER` | Presença em Linguagens e Códigos (Dia 1). | `0`, `1`, `2` | 0 | Filtro de público presente | `0` = Faltou; `1` = Presente; `2` = Eliminado. |
| `tp_presenca_mt` | `INTEGER` | Presença em Matemática (Dia 2). | `0`, `1`, `2` | 0 | Filtro de público presente | `0` = Faltou; `1` = Presente; `2` = Eliminado. |

### 5.5.1 Distribuição de Presença e Abstenção

| Prova / Dia | Faltou (`0`) | Presente (`1`) | Eliminado (`2`) | Taxa de Abstenção |
|---|---:|---:|---:|---:|
| **Dia 1** (`CH` e `LC`) | 1.106.714 (28,13%) | 2.822.643 (71,75%) | 4.598 (0,12%) | **28,13%** |
| **Dia 2** (`CN` e `MT`) | 1.239.316 (31,50%) | 2.692.427 (68,44%) | 2.212 (0,06%) | **31,50%** |

> **Comportamento identificado:** A abstenção aumentou em 3,37 pontos percentuais do primeiro para o segundo dia de prova, refletindo o padrão histórico de desistência entre as etapas do exame.

---

## 5.6 Desempenho (Notas)

As notas das provas objetivas são calculadas pela Teoria de Resposta ao Item (TRI), variando em uma escala típica de 0 a ~1000 pontos. A nota de Redação é obtida pela soma das 5 competências avaliadas por corretores humanos (0 a 1000 pontos).

| Variável | Tipo | Área do Conhecimento | Escala Teórica | Nulos | Média | Mediana | Desvio Padrão |
|---|---|---|:---:|---:|---:|---:|---:|
| `nu_nota_cn` | `NUMERIC(6,2)` | Ciências da Natureza | 0 a 1000 (TRI) | 1.241.528 (31,56%) | 495,75 | 493,90 | 87,93 |
| `nu_nota_ch` | `NUMERIC(6,2)` | Ciências Humanas | 0 a 1000 (TRI) | 1.111.312 (28,25%) | 523,35 | 530,40 | 88,57 |
| `nu_nota_lc` | `NUMERIC(6,2)` | Linguagens e Códigos | 0 a 1000 (TRI) | 1.111.312 (28,25%) | 518,15 | 523,10 | 75,45 |
| `nu_nota_mt` | `NUMERIC(6,2)` | Matemática | 0 a 1000 (TRI) | 1.241.528 (31,56%) | 533,84 | 523,60 | 131,65 |
| `nu_nota_redacao` | `NUMERIC(6,2)` | Redação | 0 a 1000 (Analítica) | 1.111.312 (28,25%) | 617,80 | 620,00 | 214,62 |

### 5.6.1 Relação entre Valores Nulos e Presença
Os valores nulos nas colunas de notas **não constituem perda acidental de dados**, mas sim a ausência do participante na prova:
- Candidatos que faltaram (`TP_PRESENCA = 0`) ou foram eliminados (`TP_PRESENCA = 2`) recebem `NULL` nas notas.
- Para análises de desempenho acadêmico, o universo deve ser restringido a participantes presentes em todas as provas (`TP_PRESENCA = 1`).

---

# 6. Variáveis Selecionadas e Justificativas

Das 76 colunas originais do INEP, 18 variáveis estratégicas foram selecionadas para compor a base de análise do EduDataBR:

| # | Variável | Categoria | Justificativa da Seleção |
|:---:|---|---|---|
| 1 | `nu_inscricao` | Identificação | Garantir unicidade dos registros e rastreabilidade individual. |
| 2 | `nu_ano` | Identificação | Controle temporal de versão do exame (2023). |
| 3 | `tp_faixa_etaria` | Demográfica | Analisar se a maturidade e defasagem idade-série afetam o desempenho. |
| 4 | `tp_sexo` | Demográfica | Investigar disparidades de gênero por área do conhecimento (ex.: Matemática vs. Linguagens). |
| 5 | `tp_cor_raca` | Demográfica | Avaliar índices de equidade racial e acesso ao ensino superior. |
| 6 | `sg_uf_prova` | Geográfica | Identificar assimetrias regionais entre estados e macrorregiões. |
| 7 | `tp_escola` | Educacional | Mensurar o gap educacional entre estudantes de escolas públicas e privadas. |
| 8 | `tp_presenca_cn` | Participação | Filtrar candidatos válidos do 2º dia e estudar taxas de abstenção. |
| 9 | `tp_presenca_ch` | Participação | Filtrar candidatos válidos do 1º dia e estudar taxas de abstenção. |
| 10 | `tp_presenca_lc` | Participação | Validar realização da prova de linguagens. |
| 11 | `tp_presenca_mt` | Participação | Validar realização da prova de matemática. |
| 12 | `nu_nota_cn` | Desempenho | Avaliação quantitativa em Ciências da Natureza. |
| 13 | `nu_nota_ch` | Desempenho | Avaliação quantitativa em Ciências Humanas. |
| 14 | `nu_nota_lc` | Desempenho | Avaliação quantitativa em Linguagens e Códigos. |
| 15 | `nu_nota_mt` | Desempenho | Avaliação quantitativa em Matemática. |
| 16 | `nu_nota_redacao` | Desempenho | Avaliação qualitativa e argumentativa (critério decisivo em vestibulares/SISU). |
| 17 | `q006` | Socioeconômica | Principal proxy de nível socioeconômico e poder aquisitivo familiar. |
| 18 | `q025` | Socioeconômica | Proxy de infraestrutura tecnológica e inclusão digital no lar. |

---

# 7. Variáveis Excluídas e Critérios

| Grupo de Variáveis Excluídas | Exemplos | Motivo da Exclusão |
|---|---|---|
| **Identificadores Locais de Escola** | `co_escola`, `co_municipio_esc`, `no_municipio_esc` | Mais de 60% dos participantes já concluíram o EM e apresentam dados escolares nulos; focar na UF garante integridade. |
| **Gabaritos e Vetores de Resposta** | `tx_respostas_*`, `tx_gabarito_*` | O foco da análise está no desempenho consolidado (TRI e notas) e não na calibração psicométrica item a item. |
| **Detalhes de Aplicação e Recursos** | `in_treineiro`, `in_braille`, `tp_lingua` | Variáveis especializadas ou de baixa representatividade para as perguntas centrais de negócio desta fase. |
| **Questões de Bens Materiais** | `q007` a `q024` (geladeira, carro, TV) | A renda familiar (`q006`) e o acesso à internet (`q025`) já sintetizam com alta fidelidade a vulnerabilidade socioeconômica. |

---

# 8. Transformações Realizadas

| Variável Original | Transformação | Variável Resultante | Motivo |
|---|---|---|---|
| `MICRODADOS_ENEM_2023.csv` | Seleção de 18 colunas com Pandas (`usecols`) e filtro de encoding | `microdados_enem_2023_reduzido.csv` | Reduzir uso de memória de ~3.5 GB para ~300 MB, viabilizando execução local ágil. |
| `tp_sexo`, `sg_uf_prova` | Padronização em tipos SQL `CHAR(1)` e `CHAR(2)` | Campos relacionais | Otimização de armazenamento e integridade referencial no PostgreSQL. |
| `nu_nota_*` | Mapeamento para `NUMERIC(6,2)` | Campos relacionais | Precisão decimal exata para cálculos de média e dispersão. |

---

# 9. Variáveis Derivadas Planejadas (Feature Engineering)

| Variável Derivada | Variáveis de Origem | Regra de Criação | Objetivo Analítico |
|---|---|---|---|
| `nu_nota_media_geral` | `nu_nota_*` (5 provas) | Média aritmética simples das 5 notas | Variável target unificada de desempenho global do candidato. |
| `classe_renda` | `q006` | Agrupamento em Baixa (`A`-`C`), Média (`D`-`G`) e Alta (`H`-`Q`) | Facilitar visualização em gráficos e mitigar granularidade excessiva. |
| `in_vulnerabilidade` | `q006`, `q025` | `1` se renda $\le$ 1,5 SM e sem internet, senão `0` | Identificar o segmento em extrema vulnerabilidade socioeducacional. |
| `fl_presente_total` | `tp_presenca_*` (as 4) | `1` se todas iguais a `1`, senão `0` | Filtro rápido para criação da base analítica final (*complete cases*). |

---

# 10. Observações e Decisões Técnicas

1. **Privacidade INEP**: A ausência da idade contínua e dados de município da escola reflete as diretrizes da LGPD aplicadas pelo INEP a partir de 2020.
2. **TRI vs. Redação**: As provas objetivas utilizam TRI (Teoria de Resposta ao Item), onde uma mesma quantidade de acertos pode gerar notas distintas conforme a coerência pedagógica das respostas. A Redação possui escala aditiva clássica de 0 a 1000.
3. **Público de Análise**: Decidiu-se que as análises de desempenho socioeconômico excluirão participantes faltantes (`NULL` nas notas), enquanto análises de evasão/abstenção utilizarão todos os 3.933.955 registros.

---

# 11. Histórico de Atualizações

| Data | Responsável | Alteração Realizada |
|---|---|---|
| 2026-08-10 | Gustavo Saraiva | Estruturação inicial do dicionário de dados. |
| 2026-08-12 | Gustavo Saraiva | Documentação de características socioeconômicas (`q006`, `q025`). |
| 2026-09-21 | Gustavo Saraiva | Conclusão integral do dicionário: correção dos códigos de `tp_escola` (1, 2, 3), inclusão de `sg_uf_prova`, documentação de participação e notas com distribuições reais, justificativa das variáveis selecionadas/excluídas e plano de variáveis derivadas. |
