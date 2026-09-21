-- View analítica: vw_enem_presentes
-- Filtra exclusivamente candidatos presentes em todas as 4 provas e na redação (~2,69 milhões de registros)
-- Adiciona cálculo da nota média geral e rótulos amigáveis para consumo por ferramentas de BI e Python

CREATE OR REPLACE VIEW vw_enem_presentes AS
SELECT
    nu_inscricao,
    nu_ano,
    tp_faixa_etaria,
    tp_sexo,
    CASE tp_cor_raca
        WHEN 0 THEN 'Não declarado'
        WHEN 1 THEN 'Branca'
        WHEN 2 THEN 'Preta'
        WHEN 3 THEN 'Parda'
        WHEN 4 THEN 'Amarela'
        WHEN 5 THEN 'Indígena'
        ELSE 'Outro'
    END AS cor_raca_desc,
    sg_uf_prova,
    tp_escola,
    CASE tp_escola
        WHEN 2 THEN 'Pública'
        WHEN 3 THEN 'Privada'
        ELSE 'Não informado / Concluído'
    END AS tipo_escola_desc,
    q006 AS faixa_renda,
    q025 AS acesso_internet,
    CASE q025
        WHEN 'B' THEN 'Com Internet'
        ELSE 'Sem Internet'
    END AS acesso_internet_desc,
    nu_nota_cn,
    nu_nota_ch,
    nu_nota_lc,
    nu_nota_mt,
    nu_nota_redacao,
    ROUND(
        (nu_nota_cn + nu_nota_ch + nu_nota_lc + nu_nota_mt + nu_nota_redacao) / 5.0, 
        2
    ) AS nu_nota_media_geral
FROM enem_microdados
WHERE tp_presenca_cn = 1
  AND tp_presenca_ch = 1
  AND tp_presenca_lc = 1
  AND tp_presenca_mt = 1;

COMMENT ON VIEW vw_enem_presentes IS 'Base de participantes que concluíram integralmente o exame, com notas médias consolidadas';
