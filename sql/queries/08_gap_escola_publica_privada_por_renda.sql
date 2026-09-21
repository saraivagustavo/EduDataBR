-- Consulta 08: Comparativo entre Escola Pública e Privada Estratificado por Renda Familiar
-- Pergunta de Negócio: PQ4 (Mediação do Gap Escolar por Renda) | Hipótese: H3
-- Técnicas: CTEs, Agregações Condicionais e Cálculo de Gap Educacional

WITH desempenho_rede_renda AS (
    SELECT
        q006 AS faixa_renda,
        
        -- Escola Pública (tp_escola = 2)
        COUNT(*) FILTER (WHERE tp_escola = 2) AS qtd_publica,
        ROUND(
            AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0) 
            FILTER (WHERE tp_escola = 2), 
            2
        ) AS media_geral_publica,
        ROUND(AVG(nu_nota_mt) FILTER (WHERE tp_escola = 2), 2) AS media_mt_publica,
        ROUND(AVG(nu_nota_redacao) FILTER (WHERE tp_escola = 2), 2) AS media_redacao_publica,

        -- Escola Privada (tp_escola = 3)
        COUNT(*) FILTER (WHERE tp_escola = 3) AS qtd_privada,
        ROUND(
            AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0) 
            FILTER (WHERE tp_escola = 3), 
            2
        ) AS media_geral_privada,
        ROUND(AVG(nu_nota_mt) FILTER (WHERE tp_escola = 3), 2) AS media_mt_privada,
        ROUND(AVG(nu_nota_redacao) FILTER (WHERE tp_escola = 3), 2) AS media_redacao_privada

    FROM enem_microdados
    WHERE tp_presenca_cn = 1 
      AND tp_presenca_ch = 1 
      AND tp_presenca_lc = 1 
      AND tp_presenca_mt = 1
      AND tp_escola IN (2, 3)
    GROUP BY q006
)
SELECT
    faixa_renda,
    qtd_publica,
    qtd_privada,
    media_geral_publica,
    media_geral_privada,
    
    -- Gap Absoluto (Privada - Pública) dentro do mesmo extrato salarial
    ROUND(media_geral_privada - media_geral_publica, 2) AS gap_geral_privada_vs_publica,
    ROUND(media_mt_privada - media_mt_publica, 2) AS gap_matematica,
    ROUND(media_redacao_privada - media_redacao_publica, 2) AS gap_redacao

FROM desempenho_rede_renda
ORDER BY faixa_renda;
