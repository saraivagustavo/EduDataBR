DROP TABLE IF EXISTS enem_microdados;

CREATE TABLE enem_microdados (
    nu_inscricao TEXT,
    nu_ano INTEGER,
    tp_faixa_etaria INTEGER,
    tp_sexo CHAR(1),
    tp_cor_raca INTEGER,
    sg_uf_prova CHAR(2),
    tp_escola INTEGER,
    tp_presenca_cn INTEGER,
    tp_presenca_ch INTEGER,
    tp_presenca_lc INTEGER,
    tp_presenca_mt INTEGER,
    nu_nota_cn NUMERIC(6,2),
    nu_nota_ch NUMERIC(6,2),
    nu_nota_lc NUMERIC(6,2),
    nu_nota_mt NUMERIC(6,2),
    nu_nota_redacao NUMERIC(6,2),
    q006 CHAR(1),
    q025 CHAR(1)
);