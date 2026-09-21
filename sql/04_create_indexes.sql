-- Script de criação de índices para otimização de consultas analíticas
-- Tabela: enem_microdados (~3,93 milhões de registros)

-- 1. Índice para agregações geográficas (por Estado / Macrorregião)
CREATE INDEX IF NOT EXISTS idx_enem_uf 
ON enem_microdados (sg_uf_prova);

-- 2. Índice para comparações de rede de ensino (Pública x Privada)
CREATE INDEX IF NOT EXISTS idx_enem_escola 
ON enem_microdados (tp_escola);

-- 3. Índice para estratificação por renda familiar
CREATE INDEX IF NOT EXISTS idx_enem_renda 
ON enem_microdados (q006);

-- 4. Índice para análises de inclusão digital
CREATE INDEX IF NOT EXISTS idx_enem_internet 
ON enem_microdados (q025);

-- 5. Índice para recortes de gênero
CREATE INDEX IF NOT EXISTS idx_enem_sexo 
ON enem_microdados (tp_sexo);

-- 6. Índice Composto de Presença (acelera o filtro dos participantes que fizeram todas as provas)
CREATE INDEX IF NOT EXISTS idx_enem_presenca_todas 
ON enem_microdados (tp_presenca_cn, tp_presenca_ch, tp_presenca_lc, tp_presenca_mt);

-- 7. Índice Parcial Avançado (Otimização PostgreSQL):
-- Indexa apenas os ~2,69 milhões de candidatos presentes em todas as provas,
-- acelerando drasticamente queries analíticas que cruzam UF, escola e renda.
CREATE INDEX IF NOT EXISTS idx_enem_presentes_analitico 
ON enem_microdados (sg_uf_prova, tp_escola, q006)
WHERE tp_presenca_cn = 1 
  AND tp_presenca_ch = 1 
  AND tp_presenca_lc = 1 
  AND tp_presenca_mt = 1;
