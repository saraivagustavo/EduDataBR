-- Consulta para obter o número total de participantes, a média das notas de matemática, redação, ciências da natureza, ciências humanas e linguagens por tipo de escola, para comparar o desempenho entre escolas públicas e privadas

SELECT
    CASE
        WHEN tp_escola = 2 THEN 'Publica'
        WHEN tp_escola = 3 THEN 'Privada'
        ELSE 'Outro' -- Não especificado ou outros tipos de escola
    END AS tipo_escola,

    ROUND(AVG(nu_nota_mt), 2) AS media_mt,
    ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
    ROUND(AVG(nu_nota_cn), 2) AS media_cn,
    ROUND(AVG(nu_nota_ch), 2) AS media_ch,
    ROUND(AVG(nu_nota_lc), 2) AS media_lc,
    COUNT(*) AS total

FROM enem_microdados
WHERE tp_presenca_mt = 1
GROUP BY tipo_escola
ORDER BY media_mt DESC;