-- 1. ¿Cuáles son las habilidades tecnológicas con el salario promedio más alto?
SELECT 
    s.skill_name, 
    ROUND(AVG(sal.salary_usd), 2) AS promedio_salarial
FROM skills s
JOIN salaries sal ON s.job_id = sal.job_id
GROUP BY s.skill_name
ORDER BY promedio_salarial DESC
LIMIT 10;

-- 2. Relación Valor/Presencia: ¿Qué tan comunes son las habilidades mejor pagadas?
-- Responde a la métrica de "Market Skill Presence" de tu dashboard estratégico.
SELECT 
    s.skill_name, 
    COUNT(DISTINCT s.job_id) AS volumen_vacantes,
    ROUND(AVG(sal.salary_usd), 2) AS promedio_salarial,
    ROUND((COUNT(DISTINCT s.job_id) * 100.0 / (SELECT COUNT(DISTINCT job_id) FROM skills)), 2) AS porcentaje_presencia
FROM skills s
JOIN salaries sal ON s.job_id = sal.job_id
GROUP BY s.skill_name
ORDER BY volumen_vacantes DESC;

-- 3. Análisis de Salario por Nivel de Experiencia (Seniority)
-- Valida los datos de tu gráfico de barras de 63k a 188k USD.
SELECT 
    experience_level, 
    ROUND(AVG(salary_usd), 2) AS salario_promedio,
    COUNT(*) AS total_posiciones
FROM jobs
join salaries on salaries.job_id= jobs.job_id 
GROUP BY experience_level
ORDER BY salario_promedio ASC;

-- 4. Top 10 Relación Salario-Demanda 
-- Cruza la popularidad con el pago para identificar nichos.
SELECT 
    s.skill_name, 
    COUNT(s.job_id) AS demanda, 
    ROUND(AVG(sal.salary_usd), 2) AS salario_promedio
FROM skills s
JOIN salaries sal ON s.job_id = sal.job_id
GROUP BY s.skill_name
HAVING demanda > 5 -- Filtramos para evitar ruidos de habilidades muy raras
ORDER BY salario_promedio DESC
LIMIT 10;
