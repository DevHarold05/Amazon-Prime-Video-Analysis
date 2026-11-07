
USE [Amazon Prime Video DW];
GO

---------------------------------------------
--1. LOAD DIMENSION TYPE
---------------------------------------------

INSERT INTO Dim_Type (type_name)
SELECT DISTINCT LTRIM(RTRIM(type))
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo
WHERE type IS NOT NULL
  AND LTRIM(RTRIM(type)) <> '';
GO

---------------------------------------------
-- 2. LOAD DIMENSION RATING
---------------------------------------------

INSERT INTO Dim_Rating (rating_name)
SELECT DISTINCT LTRIM(RTRIM(rating))
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo
WHERE rating IS NOT NULL
  AND LTRIM(RTRIM(rating)) <> '';
GO

-- ==========================================
-- 3. LOAD DIMENSION YEAR
-- ==========================================

INSERT INTO Dim_AnneeSortie (annee_sortie)
SELECT DISTINCT release_year
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo
WHERE release_year IS NOT NULL;
GO

---------------------------------------------
-- 4. LOAD DIMENSION COUNTRY
---------------------------------------------

INSERT INTO Dim_Pays (pays_nom)
SELECT DISTINCT LTRIM(RTRIM(s.value))
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo AS a
CROSS APPLY STRING_SPLIT(a.country, ',') AS s
WHERE a.country IS NOT NULL
  AND LTRIM(RTRIM(s.value)) <> '';
GO

---------------------------------------------
-- 5. LOAD DIMENSION GENRE
---------------------------------------------
INSERT INTO Dim_Genre (genre_nom)
SELECT DISTINCT LTRIM(RTRIM(s.value))
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo AS a
CROSS APPLY STRING_SPLIT(a.listed_in, ',') AS s
WHERE a.listed_in IS NOT NULL
  AND LTRIM(RTRIM(s.value)) <> '';
GO

---------------------------------------------
-- 6. LOAD FACT TABLE
---------------------------------------------

INSERT INTO Fait_Contenu (
    show_id,
    title,
    type_sk,
    rating_sk,
    annee_sk,
    duration_value,
    duration_unit
)
SELECT
    a.show_id,
    a.title,
    t.type_sk,
    r.rating_sk,
    y.annee_sk,
    TRY_CONVERT(INT,
        LEFT(a.duration, CHARINDEX(' ', a.duration + ' ') - 1)
    ),
    CASE
        WHEN a.duration LIKE '%min%' THEN 'min'
        WHEN a.duration LIKE '%Season%' THEN 'Season'
        ELSE NULL
    END
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo AS a
LEFT JOIN Dim_Type AS t
    ON LTRIM(RTRIM(a.type)) = t.type_name
LEFT JOIN Dim_Rating AS r
    ON LTRIM(RTRIM(a.rating)) = r.rating_name
LEFT JOIN Dim_AnneeSortie AS y
    ON a.release_year = y.annee_sortie;
GO

---------------------------------------------
-- 7. LOAD BRIDGE COUNTRY
---------------------------------------------

INSERT INTO Bridge_Contenu_Pays (contenu_sk, pays_sk)
SELECT DISTINCT
    f.contenu_sk,
    p.pays_sk
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo AS a
INNER JOIN Fait_Contenu AS f
    ON a.show_id = f.show_id
CROSS APPLY STRING_SPLIT(a.country, ',') AS s
INNER JOIN Dim_Pays AS p
    ON LTRIM(RTRIM(s.value)) = p.pays_nom;
GO

---------------------------------------------
-- 8. LOAD BRIDGE GENRE
---------------------------------------------

INSERT INTO Bridge_Contenu_Genre (contenu_sk, genre_sk)
SELECT DISTINCT
    f.contenu_sk,
    g.genre_sk
FROM [Amazon Prime Video DB].dbo.Stg_AmazonPrimeVideo AS a
INNER JOIN Fait_Contenu AS f
    ON a.show_id = f.show_id
CROSS APPLY STRING_SPLIT(a.listed_in, ',') AS s
INNER JOIN Dim_Genre AS g
    ON LTRIM(RTRIM(s.value)) = g.genre_nom;
GO
