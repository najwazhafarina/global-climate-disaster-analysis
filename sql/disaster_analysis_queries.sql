SELECT 
    year,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY year
ORDER BY year;

SELECT 
    disaster_type,
    COUNT(*) AS total_events
FROM disasters
GROUP BY disaster_type
ORDER BY total_events DESC;

SELECT 
    country,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY country
ORDER BY total_disasters DESC
LIMIT 10;

SELECT 
    disaster_type,
    SUM(total_deaths) AS total_deaths
FROM disasters
GROUP BY disaster_type
ORDER BY total_deaths DESC;

SELECT 
    disaster_type,
    SUM(total_damage_usd) AS total_damage
FROM disasters
GROUP BY disaster_type
ORDER BY total_damage DESC;

SELECT 
    region,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY region
ORDER BY total_disasters DESC;

SELECT 
    year,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY year
ORDER BY total_disasters DESC
LIMIT 5;

SELECT 
    region,
    disaster_type,
    COUNT(*) AS total_events
FROM disasters
GROUP BY region, disaster_type
ORDER BY region, total_events DESC;

SELECT 
    country,
    SUM(total_deaths) AS total_deaths
FROM disasters
GROUP BY country
ORDER BY total_deaths DESC
LIMIT 10;

SELECT 
    disaster_type,
    AVG(total_deaths) AS avg_deaths
FROM disasters
GROUP BY disaster_type
ORDER BY avg_deaths DESC;

SELECT 
    country,
    SUM(total_damage_usd) AS total_damage
FROM disasters
GROUP BY country
ORDER BY total_damage DESC
LIMIT 10;

SELECT 
    year,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY year
ORDER BY year;

SELECT * 
FROM disasters
LIMIT 5;

SELECT 
    disaster_type,
    COUNT(*) AS total_events,
    SUM(total_deaths) AS total_deaths,
    AVG(total_deaths) AS avg_deaths_per_event
FROM disasters
GROUP BY disaster_type
ORDER BY avg_deaths_per_event DESC;

SELECT 
    region,
    year,
    COUNT(*) AS total_disasters
FROM disasters
GROUP BY region, year
ORDER BY region, year;

SELECT 
    country,
    disaster_type,
    COUNT(*) AS total_events
FROM disasters
GROUP BY country, disaster_type
ORDER BY total_events DESC;


