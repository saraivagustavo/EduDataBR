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

> As informações apresentadas neste documento devem ser verificadas com base na documentação oficial disponibilizada pelo INEP.

---

# 3. Organização do Dicionário

As variáveis serão documentadas de acordo com sua função analítica dentro do projeto.

As categorias utilizadas inicialmente são:

- Identificação;
- Características demográficas;
- Características socioeconômicas;
- Características educacionais;
- Participação no exame;
- Desempenho;
- Outras variáveis relevantes identificadas durante o Data Understanding.

A classificação poderá ser alterada conforme a compreensão dos dados evoluir.

---

# 4. Convenções

| Campo | Descrição |
|---|---|
| **Variável** | Nome original da coluna presente na base. |
| **Tipo** | Tipo de dado utilizado no projeto. |
| **Descrição** | Significado da variável segundo a documentação oficial. |
| **Domínio** | Valores ou categorias possíveis para a variável. |
| **Nulos** | Presença e comportamento de valores ausentes. |
| **Tratamento** | Transformações ou tratamentos aplicados. |
| **Utilização** | Etapas do projeto em que a variável será utilizada. |
| **Observações** | Informações adicionais relevantes. |

---

# 5. Variáveis

## 5.1 Identificação

As variáveis desta categoria estão relacionadas à identificação do registro e à identificação do ano de realização do exame.

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `nu_inscricao` | `INTEGER` | Número de inscrição do participante no ENEM. | Numérico | A validar | A definir | Identificação do registro | Variável utilizada para identificar a inscrição na base analisada. |
| `nu_ano` | `INTEGER` | Ano de realização do exame. | `2023` | A validar | A definir | Controle temporal e identificação da edição do exame | Na base analisada pelo projeto, os registros correspondem ao ENEM 2023. |

### Observações

- `nu_inscricao` foi mantida na base utilizada pelo projeto para identificação dos registros.
- O tipo `INTEGER` corresponde ao tipo utilizado na tabela `enem_microdados` no PostgreSQL do projeto.
- A análise de valores nulos ainda será realizada na etapa de **Data Quality**.
- O tratamento definitivo das variáveis será definido após a conclusão da análise de qualidade dos dados.
- A fonte dos dados é o conjunto de Microdados do ENEM 2023 disponibilizado pelo INEP.

---

## 5.2 Características Demográficas

As variáveis desta categoria representam características demográficas dos participantes disponibilizadas nos microdados do ENEM.

A divulgação dessas informações segue as adequações de privacidade adotadas pelo INEP. Entre essas adequações está a substituição da idade individual pela variável de faixa etária, reduzindo o risco de identificação dos participantes. 

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `tp_faixa_etaria` | `INTEGER` | Faixa etária do participante. | Códigos numéricos definidos pelo INEP | A validar | A definir | Análise demográfica e comparação de desempenho entre faixas etárias | A variável representa a faixa etária, e não a idade individual do participante. |
| `tp_sexo` | `VARCHAR` | Sexo do participante. | `M` = Masculino; `F` = Feminino | A validar | A definir | Análise demográfica e comparação de desempenho | Variável categórica. |
| `tp_cor_raca` | `INTEGER` | Cor/raça declarada pelo participante. | `0` = Não declarado; `1` = Branca; `2` = Preta; `3` = Parda; `4` = Amarela; `5` = Indígena | A validar | A definir | Análise demográfica e comparação de desempenho | Variável categórica codificada. |

### Observações

- `tp_faixa_etaria` representa uma faixa etária, e não a idade individual do participante.
- `tp_sexo` utiliza códigos categóricos para representar o sexo informado pelo participante.
- `tp_cor_raca` utiliza códigos numéricos para representar as categorias de cor/raça disponibilizadas nos microdados.
- Os domínios apresentados devem ser confrontados com a documentação oficial correspondente à versão dos microdados utilizada no projeto.
- A quantidade de valores nulos de cada variável será determinada na etapa de **Data Quality**.
- O tratamento de valores ausentes ou categorias especiais será definido após a análise de qualidade dos dados.
- Nenhuma categoria será agrupada ou recodificada antes que sua necessidade seja identificada durante as análises.

---

## 5.3 Características Socioeconômicas

As variáveis desta categoria são provenientes do questionário socioeconômico associado aos microdados do ENEM e representam características relacionadas ao contexto socioeconômico dos participantes.

Essas informações serão utilizadas posteriormente para investigar possíveis relações entre características socioeconômicas e o desempenho dos participantes no exame.

| Variável | Tipo | Descrição | Domínio observado | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `q006` | `VARCHAR` | Faixa de renda mensal da família do participante, conforme categorias apresentadas no questionário socioeconômico. | `A` a `Q` | 0 | A definir | Análise socioeconômica e comparação de desempenho | Variável categórica com 17 categorias distintas. |
| `q025` | `VARCHAR` | Informação relacionada à disponibilidade de acesso à internet no domicílio do participante. | `A` e `B` | 0 | A definir | Análise de acesso à tecnologia e comparação de desempenho | Variável categórica com 2 categorias distintas. |

### 5.3.1 Domínio — `q006`

A variável `q006` representa a faixa de renda mensal da família do participante, conforme as categorias apresentadas no questionário socioeconômico do ENEM.

| Código | Categoria de renda mensal familiar |
|---|---|
| `A` | Nenhuma renda |
| `B` | Até R$ 1.320,00 |
| `C` | De R$ 1.320,01 até R$ 1.980,00 |
| `D` | De R$ 1.980,01 até R$ 2.640,00 |
| `E` | De R$ 2.640,01 até R$ 3.300,00 |
| `F` | De R$ 3.300,01 até R$ 3.960,00 |
| `G` | De R$ 3.960,01 até R$ 5.280,00 |
| `H` | De R$ 5.280,01 até R$ 6.600,00 |
| `I` | De R$ 6.600,01 até R$ 7.920,00 |
| `J` | De R$ 7.920,01 até R$ 9.240,00 |
| `K` | De R$ 9.240,01 até R$ 10.560,00 |
| `L` | De R$ 10.560,01 até R$ 11.880,00 |
| `M` | De R$ 11.880,01 até R$ 13.200,00 |
| `N` | De R$ 13.200,01 até R$ 15.840,00 |
| `O` | De R$ 15.840,01 até R$ 19.800,00 |
| `P` | De R$ 19.800,01 até R$ 26.400,00 |
| `Q` | Acima de R$ 26.400,00 |

### 5.3.2 Distribuição da variável `q006`

A distribuição abaixo foi obtida diretamente a partir da tabela `enem_microdados` no PostgreSQL.

| Código | Categoria | Quantidade | Percentual |
|---|---|---:|---:|
| `A` | Nenhuma renda | 268.053 | 6,81% |
| `B` | Até R$ 1.320,00 | 1.245.271 | 31,65% |
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
| `Q` | Acima de R$ 26.400,00 | 51.489 | 1,31% |

**Total:** 3.933.955 registros.

### 5.3.3 Domínio — `q025`

A variável `q025` indica se o participante possui acesso à internet em seu domicílio, conforme as categorias apresentadas no questionário socioeconômico do ENEM.

| Código | Categoria |
|---|---|
| `A` | Não |
| `B` | Sim |

### 5.3.4 Distribuição da variável `q025`

A distribuição abaixo foi obtida diretamente a partir da tabela `enem_microdados` no PostgreSQL.

| Código | Categoria | Quantidade | Percentual |
|---|---|---:|---:|
| `A` | Não | 375.504 | 9,55% |
| `B` | Sim | 3.558.451 | 90,45% |

**Total:** 3.933.955 registros.

### 5.3.5 Qualidade dos dados

As variáveis `q006` e `q025` foram verificadas quanto à presença de valores `NULL` na tabela analisada.

| Variável | Total de registros | Preenchidos | Nulos |
|---|---:|---:|---:|
| `q006` | 3.933.955 | 3.933.955 | 0 |
| `q025` | 3.933.955 | 3.933.955 | 0 |

Não foram identificados valores `NULL` nas duas variáveis durante a análise realizada.

### Observações

- `q006` apresenta 17 categorias distintas (`A` a `Q`).
- `q025` apresenta 2 categorias distintas (`A` e `B`).
- As quantidades e percentuais apresentados foram obtidos diretamente por meio de consultas SQL realizadas no PostgreSQL.
- Ambas as variáveis possuem 3.933.955 registros preenchidos na tabela analisada.
- Os códigos das categorias foram mantidos em seu formato original.
- O tratamento das variáveis será definido nas etapas posteriores do projeto.
- Nenhuma categoria será agrupada previamente sem uma justificativa analítica documentada.
- As distribuições apresentadas nesta seção são descritivas e não representam, isoladamente, relações de causa e efeito.

---

## 5.4 Características Educacionais

As variáveis desta categoria representam características relacionadas ao contexto educacional dos participantes do ENEM.

Essas informações poderão ser utilizadas para investigar diferenças de desempenho entre participantes com diferentes características e trajetórias educacionais.

| Variável | Tipo | Descrição | Domínio observado | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `tp_escola` | `INTEGER` | Tipo de escola do participante. | Códigos numéricos definidos pelo INEP | A validar | A definir | Análise do desempenho por tipo de escola | Variável categórica codificada. |

### 5.4.1 Domínio — `tp_escola`

A variável `tp_escola` representa o tipo de escola associado ao participante, conforme a classificação utilizada nos microdados do ENEM.

| Código | Categoria |
|---|---|
| `A` | Não respondeu |
| `B` | Pública |
| `C` | Privada |

> Os códigos e suas respectivas categorias devem ser confirmados a partir da documentação oficial dos Microdados do ENEM 2023 antes de serem utilizados nas análises.

### 5.4.2 Distribuição da variável `tp_escola`

A distribuição da variável será obtida diretamente a partir da tabela `enem_microdados` no PostgreSQL.

```sql
SELECT
    tp_escola,
    COUNT(*) AS quantidade,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentual
FROM enem_microdados
GROUP BY tp_escola
ORDER BY tp_escola;
```

---

## 5.5 Participação no ENEM

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `PREENCHER` | — | — | — | — | — | — | — |

---

## 5.6 Desempenho

| Variável | Tipo | Descrição | Domínio | Nulos | Tratamento | Utilização | Observações |
|---|---|---|---|---|---|---|---|
| `PREENCHER` | — | — | — | — | — | — | — |

---

# 6. Variáveis Selecionadas

Esta seção apresenta as variáveis efetivamente selecionadas para o desenvolvimento das análises do EduDataBR.

A seleção deverá ser baseada nas perguntas de negócio, na qualidade dos dados e na relevância analítica de cada variável.

| Variável | Justificativa da Seleção | Etapa |
|---|---|---|
| `PREENCHER` | `PREENCHER` | `PREENCHER` |

---

# 7. Variáveis Excluídas

Variáveis inicialmente disponíveis na base que não forem utilizadas no projeto poderão ser registradas nesta seção.

| Variável | Motivo da Exclusão | Observações |
|---|---|---|
| `PREENCHER` | `PREENCHER` | `PREENCHER` |

> A exclusão de uma variável não significa necessariamente que ela seja irrelevante. A decisão considera o escopo e os objetivos específicos do EduDataBR.

---

# 8. Transformações

As transformações realizadas sobre as variáveis serão registradas nesta seção.

| Variável Original | Transformação | Variável Resultante | Motivo |
|---|---|---|---|
| `PREENCHER` | `PREENCHER` | `PREENCHER` | `PREENCHER` |

---

# 9. Variáveis Derivadas

Variáveis criadas durante o processo de Feature Engineering serão documentadas separadamente das variáveis originais.

| Variável | Origem | Regra de Criação | Tipo | Objetivo |
|---|---|---|---|---|
| `PREENCHER` | `PREENCHER` | `PREENCHER` | `PREENCHER` | `PREENCHER` |

---

# 10. Observações e Decisões

Esta seção será utilizada para registrar observações importantes relacionadas à interpretação das variáveis.

Exemplos de informações que poderão ser registradas:

- alterações de nomenclatura;
- mudanças de tipo;
- códigos especiais;
- valores ausentes;
- categorias agrupadas;
- variáveis utilizadas apenas para determinadas análises;
- limitações identificadas na interpretação dos dados.

---

# 11. Histórico de Atualizações

| Data | Alteração |
|---|---|
| 2026-08-10 | Estrutura inicial do dicionário de dados criada. |

> Este documento será atualizado conforme novas variáveis forem analisadas e selecionadas para o projeto.
