-- Consulta 06: Ranking de Desempenho por Estado utilizando Window Functions
-- Pergunta de Negócio: PQ5 (Assimetrias Geográficas) | Hipótese: H5
-- Técnicas: Window Functions (RANK, DENSE_RANK, NTILE, AVG OVER) e CTE

WITH medias_por_estado AS (
    SELECT
        sg_uf_prova,
        COUNT(*) AS total_participantes,
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
    GROUP BY sg_uf_prova
)
SELECT
    sg_uf_prova,
    total_participantes,
    media_matematica,
    media_redacao,
    media_geral,
    
    -- Ranking nacional baseado na média geral
    RANK() OVER (ORDER BY media_geral DESC) AS ranking_nacional,
    
    -- Divisão dos 27 estados em 4 quartis de desempenho
    -- 1 = Quartil Superior (Top 25% estados), 4 = Quartil Inferior
    NTILE(4) OVER (ORDER BY media_geral DESC) AS quartil_desempenho,
    
    -- Média nacional ponderada calculada via window function para referência
    ROUND(
        AVG(media_geral) OVER (), 
        2
    ) AS media_nacional_referencia,
    
    -- Diferença do estado em relação à média nacional
    ROUND(
        media_geral - AVG(media_geral) OVER (), 
        2
    ) AS diferenca_media_nacional

FROM medias_por_estado
ORDER BY ranking_nacional;
