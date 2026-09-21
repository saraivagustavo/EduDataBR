-- Consulta 10: Determinantes Socioeconômicos da Evasão entre os Dias de Prova
-- Pergunta de Negócio: PQ8 (Abstenção e Evasão) | Hipótese: H6
-- Técnicas: Agregações com FILTER, Cálculo de Taxas de Evasão e Ordenação Analítica

SELECT
    q006 AS faixa_renda,
    CASE q025
        WHEN 'B' THEN 'Com Internet'
        ELSE 'Sem Internet'
    END AS status_internet,
    
    -- Total de participantes inscritos no grupo
    COUNT(*) AS total_inscritos,

    -- Compareceram no 1º Domingo (Linguagens/Humanas/Redação)
    COUNT(*) FILTER (WHERE tp_presenca_lc = 1) AS presentes_dia_1,

    -- Compareceram no 1º Domingo MAS faltaram no 2º Domingo (Abandono/Evasão)
    COUNT(*) FILTER (WHERE tp_presenca_lc = 1 AND tp_presenca_mt = 0) AS evadidos_dia_2,

    -- Taxa de Evasão entre os domingos (%)
    ROUND(
        COUNT(*) FILTER (WHERE tp_presenca_lc = 1 AND tp_presenca_mt = 0) * 100.0 / 
        NULLIF(COUNT(*) FILTER (WHERE tp_presenca_lc = 1), 0),
        2
    ) AS taxa_evasao_segundo_dia_pct,

    -- Taxa de Abstenção Total (faltou em ambos os dias)
    ROUND(
        COUNT(*) FILTER (WHERE tp_presenca_lc = 0 AND tp_presenca_mt = 0) * 100.0 / COUNT(*),
        2
    ) AS taxa_abstencao_total_pct

FROM enem_microdados
GROUP BY q006, q025
ORDER BY q006, status_internet;
