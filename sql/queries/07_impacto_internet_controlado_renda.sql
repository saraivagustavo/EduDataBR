-- Consulta 07: Impacto do Acesso à Internet Controlado por Faixa de Renda Familiar
-- Pergunta de Negócio: PQ2 (Inclusão Digital) | Hipótese: H2
-- Técnicas: CTEs, Agregações Condicionais e Cálculo de Ganho de Desempenho

WITH desempenho_estratificado AS (
    SELECT
        q006 AS faixa_renda,
        
        -- Participantes e notas COM internet
        COUNT(*) FILTER (WHERE q025 = 'B') AS total_com_internet,
        ROUND(AVG(nu_nota_mt) FILTER (WHERE q025 = 'B'), 2) AS media_mt_com_internet,
        ROUND(AVG(nu_nota_redacao) FILTER (WHERE q025 = 'B'), 2) AS media_redacao_com_internet,
        ROUND(
            AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0) 
            FILTER (WHERE q025 = 'B'), 
            2
        ) AS media_geral_com_internet,

        -- Participantes e notas SEM internet
        COUNT(*) FILTER (WHERE q025 = 'A') AS total_sem_internet,
        ROUND(AVG(nu_nota_mt) FILTER (WHERE q025 = 'A'), 2) AS media_mt_sem_internet,
        ROUND(AVG(nu_nota_redacao) FILTER (WHERE q025 = 'A'), 2) AS media_redacao_sem_internet,
        ROUND(
            AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0) 
            FILTER (WHERE q025 = 'A'), 
            2
        ) AS media_geral_sem_internet

    FROM enem_microdados
    WHERE tp_presenca_cn = 1 
      AND tp_presenca_ch = 1 
      AND tp_presenca_lc = 1 
      AND tp_presenca_mt = 1
    GROUP BY q006
)
SELECT
    faixa_renda,
    total_com_internet,
    total_sem_internet,
    media_geral_com_internet,
    media_geral_sem_internet,
    
    -- Ganho absoluto de nota por ter internet dentro da mesma faixa salarial
    ROUND(media_geral_com_internet - media_geral_sem_internet, 2) AS ganho_geral_absoluto,
    ROUND(media_mt_com_internet - media_mt_sem_internet, 2) AS ganho_matematica_absoluto,
    ROUND(media_redacao_com_internet - media_redacao_sem_internet, 2) AS ganho_redacao_absoluto,

    -- Ganho percentual relativo
    ROUND(
        (media_geral_com_internet - media_geral_sem_internet) * 100.0 / NULLIF(media_geral_sem_internet, 0),
        2
    ) AS ganho_percentual_relativo

FROM desempenho_estratificado
ORDER BY faixa_renda;
