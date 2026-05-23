-- Consulta para verificar se a relação entre renda familiar e desempenho dos participantes segue um padrão, analisando a média das notas de matemática, redação, ciências da natureza, ciências humanas e linguagens por faixa de renda

SELECT
    q006 AS faixa_renda,
    COUNT(*) AS total_participantes,
    ROUND(AVG(nu_nota_mt), 2) AS media_matematica,
    ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
    ROUND(AVG(nu_nota_cn), 2) AS media_cn,
    ROUND(AVG(nu_nota_ch), 2) AS media_ch,
    ROUND(AVG(nu_nota_lc), 2) AS media_lc
FROM enem_microdados
WHERE tp_presenca_cn = 1
  AND tp_presenca_ch = 1
  AND tp_presenca_lc = 1
  AND tp_presenca_mt = 1
GROUP BY q006
ORDER BY q006;
