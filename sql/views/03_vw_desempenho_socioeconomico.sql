-- View analítica: vw_desempenho_socioeconomico
-- Consolida métricas de desempenho cruzando faixa de renda familiar e acesso à internet

CREATE OR REPLACE VIEW vw_desempenho_socioeconomico AS
SELECT
    q006 AS faixa_renda,
    CASE q025
        WHEN 'B' THEN 'Com Internet'
        ELSE 'Sem Internet'
    END AS status_internet,
    
    COUNT(*) AS total_participantes,
    ROUND(AVG(nu_nota_mt), 2) AS media_matematica,
    ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
    ROUND(AVG(nu_nota_cn), 2) AS media_natureza,
    ROUND(AVG(nu_nota_ch), 2) AS media_humanas,
    ROUND(AVG(nu_nota_lc), 2) AS media_linguagens,
    ROUND(
        AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0),
        2
    ) AS media_geral

FROM enem_microdados
WHERE tp_presenca_cn = 1 
  AND tp_presenca_ch = 1 
  AND tp_presenca_lc = 1 
  AND tp_presenca_mt = 1
GROUP BY q006, q025
ORDER BY q006, status_internet;

COMMENT ON VIEW vw_desempenho_socioeconomico IS 'Métricas de desempenho fatiadas por renda familiar e inclusão digital';
