-- Análise de desempenho dos participantes com base no acesso à internet, verificando se há diferenças significantes nas médias das notas de matemática, redação, ciências da natureza, ciências humanas e linguagens entre os participantes que têm acesso à internet e os que não têm acesso à internet
-- A: não tem acesso à internet 
-- B: tem acesso à internet

SELECT
    q025 AS acesso_internet,

    ROUND(AVG(nu_nota_mt), 2) AS media_mt,
    ROUND(AVG(nu_nota_redacao), 2) AS media_redacao,
    ROUND(AVG(nu_nota_cn), 2) AS media_cn,
    ROUND(AVG(nu_nota_ch), 2) AS media_ch,
    ROUND(AVG(nu_nota_lc), 2) AS media_lc,
    COUNT(*) AS total

FROM enem_microdados
WHERE tp_presenca_mt = 1
GROUP BY q025;