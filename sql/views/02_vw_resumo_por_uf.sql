-- View analítica: vw_resumo_por_uf
-- Agrega métricas consolidadas de participação, absenteísmo e notas por estado

CREATE OR REPLACE VIEW vw_resumo_por_uf AS
SELECT
    sg_uf_prova,
    COUNT(*) AS total_inscritos,
    
    -- Participantes presentes em todas as provas
    COUNT(*) FILTER (
        WHERE tp_presenca_cn = 1 AND tp_presenca_ch = 1 AND tp_presenca_lc = 1 AND tp_presenca_mt = 1
    ) AS total_presentes_todos_dias,
    
    -- Taxa de presença efetiva (%)
    ROUND(
        COUNT(*) FILTER (
            WHERE tp_presenca_cn = 1 AND tp_presenca_ch = 1 AND tp_presenca_lc = 1 AND tp_presenca_mt = 1
        ) * 100.0 / COUNT(*),
        2
    ) AS taxa_presenca_pct,
    
    -- Taxa de abstenção no 2º dia de quem compareceu no 1º dia (Evasão entre domingos)
    ROUND(
        COUNT(*) FILTER (
            WHERE tp_presenca_lc = 1 AND tp_presenca_mt = 0
        ) * 100.0 / NULLIF(COUNT(*) FILTER (WHERE tp_presenca_lc = 1), 0),
        2
    ) AS taxa_evasao_segundo_dia_pct,

    -- Médias das notas dos participantes presentes
    ROUND(AVG(nu_nota_cn), 2) AS media_cn,
    ROUND(AVG(nu_nota_ch), 2) AS media_ch,
    ROUND(AVG(nu_nota_lc), 2) AS media_lc,
    ROUND(AVG(nu_nota_mt), 2) AS media_mt,
    ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
    ROUND(
        AVG((nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0),
        2
    ) AS media_geral

FROM enem_microdados
GROUP BY sg_uf_prova;

COMMENT ON VIEW vw_resumo_por_uf IS 'Métricas agregadas de participação, evasão e desempenho médio por Unidade da Federação';
