-- Consulta para obter o número total de participantes, a média das notas de matemática, redação, ciências da natureza, ciências humanas e linguagens por estado

SELECT
    sg_uf_prova,
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
GROUP BY sg_uf_prova
ORDER BY media_matematica DESC;