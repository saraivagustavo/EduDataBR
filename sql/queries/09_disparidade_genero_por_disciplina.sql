-- Consulta 09: Disparidade de Desempenho por Gênero nas 5 Áreas do Conhecimento
-- Pergunta de Negócio: PQ6 (Recortes Demográficos e Afinidades) | Hipótese: H4
-- Técnicas: Agregações Condicionais, CTEs e Cálculo de Diferencial Relativo

WITH desempenho_sexo AS (
    SELECT
        tp_sexo,
        COUNT(*) AS total_participantes,
        ROUND(AVG(nu_nota_cn), 2) AS media_ciencias_natureza,
        ROUND(AVG(nu_nota_ch), 2) AS media_ciencias_humanas,
        ROUND(AVG(nu_nota_lc), 2) AS media_linguagens_codigos,
        ROUND(AVG(nu_nota_mt), 2) AS media_matematica,
        ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
        ROUND(
            AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0),
            2
        ) AS media_geral
    FROM enem_microdados
    WHERE tp_presenca_cn = 1 
      AND tp_presenca_ch = 1 
      AND tp_presenca_lc = 1 
      AND tp_presenca_mt = 1
    GROUP BY tp_sexo
)
SELECT
    tp_sexo,
    total_participantes,
    media_matematica,
    media_ciencias_natureza,
    media_linguagens_codigos,
    media_ciencias_humanas,
    media_redacao,
    media_geral
FROM desempenho_sexo;

-- Comparação Direta do Gap (Feminino - Masculino):
-- Valores positivos indicam vantagem feminina; valores negativos indicam vantagem masculina.
WITH medias AS (
    SELECT
        ROUND(AVG(nu_nota_mt) FILTER (WHERE tp_sexo = 'F') - AVG(nu_nota_mt) FILTER (WHERE tp_sexo = 'M'), 2) AS gap_matematica,
        ROUND(AVG(nu_nota_cn) FILTER (WHERE tp_sexo = 'F') - AVG(nu_nota_cn) FILTER (WHERE tp_sexo = 'M'), 2) AS gap_natureza,
        ROUND(AVG(nu_nota_lc) FILTER (WHERE tp_sexo = 'F') - AVG(nu_nota_lc) FILTER (WHERE tp_sexo = 'M'), 2) AS gap_linguagens,
        ROUND(AVG(nu_nota_ch) FILTER (WHERE tp_sexo = 'F') - AVG(nu_nota_ch) FILTER (WHERE tp_sexo = 'M'), 2) AS gap_humanas,
        ROUND(AVG(nu_nota_redacao) FILTER (WHERE tp_sexo = 'F') - AVG(nu_nota_redacao) FILTER (WHERE tp_sexo = 'M'), 2) AS gap_redacao
    FROM enem_microdados
    WHERE tp_presenca_cn = 1 
      AND tp_presenca_ch = 1 
      AND tp_presenca_lc = 1 
      AND tp_presenca_mt = 1
)
SELECT * FROM medias;
