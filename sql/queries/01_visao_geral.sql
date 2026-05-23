-- Consulta para obter a visão geral do número total de registros e o número de participantes presentes em todas as provas

SELECT
    COUNT(*) AS total_registros,
    COUNT(*) FILTER (
        WHERE tp_presenca_cn = 1
          AND tp_presenca_ch = 1
          AND tp_presenca_lc = 1
          AND tp_presenca_mt = 1
    ) AS participantes_presentes
FROM enem_microdados;