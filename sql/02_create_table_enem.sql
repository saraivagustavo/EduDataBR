-- Script DDL para criação da tabela enem_microdados no banco edudatabr
-- Tipagem refinada e constraints baseadas na auditoria de qualidade de dados

DROP TABLE IF EXISTS enem_microdados CASCADE;

CREATE TABLE enem_microdados (
    nu_inscricao VARCHAR(12) PRIMARY KEY,
    nu_ano INTEGER NOT NULL,
    tp_faixa_etaria INTEGER NOT NULL,
    tp_sexo CHAR(1) NOT NULL,
    tp_cor_raca INTEGER NOT NULL,
    sg_uf_prova CHAR(2) NOT NULL,
    tp_escola INTEGER NOT NULL,
    tp_presenca_cn INTEGER NOT NULL,
    tp_presenca_ch INTEGER NOT NULL,
    tp_presenca_lc INTEGER NOT NULL,
    tp_presenca_mt INTEGER NOT NULL,
    nu_nota_cn NUMERIC(6,2),
    nu_nota_ch NUMERIC(6,2),
    nu_nota_lc NUMERIC(6,2),
    nu_nota_mt NUMERIC(6,2),
    nu_nota_redacao NUMERIC(6,2),
    q006 CHAR(1) NOT NULL,
    q025 CHAR(1) NOT NULL
);

COMMENT ON TABLE enem_microdados IS 'Microdados reduzidos do ENEM 2023 com 18 variáveis analíticas essenciais';
COMMENT ON COLUMN enem_microdados.nu_inscricao IS 'Número de inscrição unívoco do participante';
COMMENT ON COLUMN enem_microdados.tp_escola IS 'Tipo de escola: 1=Não respondeu, 2=Pública, 3=Privada';
COMMENT ON COLUMN enem_microdados.q006 IS 'Faixa de renda familiar mensal (A até Q)';
COMMENT ON COLUMN enem_microdados.q025 IS 'Acesso à internet em domicílio (A=Não, B=Sim)';