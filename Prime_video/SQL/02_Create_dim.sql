
USE [Amazon Prime Video DW];
GO

-- Dimension Type
CREATE TABLE Dim_Type (
    type_sk INT IDENTITY(1,1) PRIMARY KEY,
    type_name NVARCHAR(50) UNIQUE
);
GO

-- Dimension Rating
CREATE TABLE Dim_Rating (
    rating_sk INT IDENTITY(1,1) PRIMARY KEY,
    rating_name NVARCHAR(50) UNIQUE
);
GO

-- Dimension Annee Sortie
CREATE TABLE Dim_AnneeSortie (
    annee_sk INT IDENTITY(1,1) PRIMARY KEY,
    annee_sortie INT UNIQUE
);
GO

-- Dimension Pays
CREATE TABLE Dim_Pays (
    pays_sk INT IDENTITY(1,1) PRIMARY KEY,
    pays_nom NVARCHAR(150) UNIQUE
);
GO

-- Dimension Genre
CREATE TABLE Dim_Genre (
    genre_sk INT IDENTITY(1,1) PRIMARY KEY,
    genre_nom NVARCHAR(150) UNIQUE
);
GO
