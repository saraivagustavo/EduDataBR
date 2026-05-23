COPY enem_microdados
FROM 'C:/CAMINHO/DO/SEU/PROJETO/edudatabr/data/interim/microdados_enem_2023_reduzido.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';