
USE [Amazon Prime Video DW];
GO

CREATE TABLE Fait_Contenu (
    contenu_sk INT IDENTITY(1,1) PRIMARY KEY,
    show_id VARCHAR(20) NOT NULL UNIQUE,
    title NVARCHAR(500) NOT NULL,
    type_sk INT,
    rating_sk INT,
    annee_sk INT,
    duration_value INT,
    duration_unit NVARCHAR(30),

    CONSTRAINT FK_Contenu_Type
        FOREIGN KEY (type_sk)
        REFERENCES Dim_Type(type_sk),

    CONSTRAINT FK_Contenu_Rating
        FOREIGN KEY (rating_sk)
        REFERENCES Dim_Rating(rating_sk),

    CONSTRAINT FK_Contenu_Annee
        FOREIGN KEY (annee_sk)
        REFERENCES Dim_AnneeSortie(annee_sk)
);
GO
