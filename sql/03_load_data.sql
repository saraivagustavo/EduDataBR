-- Script DML para importação dos dados reduzidos na tabela enem_microdados
-- Total esperado: 3.933.955 registros

-- Opção 1: Execução direta no servidor PostgreSQL (pgAdmin / DBeaver / Query Tool)
COPY enem_microdados
FROM 'C:/Users/User/Desktop/edudatabr/data/interim/microdados_enem_2023_reduzido.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- Opção 2: Execução via terminal cliente psql (não requer privilégios de sistema de arquivos do servidor)
-- \copy enem_microdados FROM 'C:/Users/User/Desktop/edudatabr/data/interim/microdados_enem_2023_reduzido.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

-- Verificação rápida pós-carga:
-- SELECT COUNT(*) AS total_registros FROM enem_microdados;