
USE [Amazon Prime Video DW];
GO

-- Bridge Content Country
CREATE TABLE Bridge_Contenu_Pays (
    contenu_sk INT NOT NULL,
    pays_sk INT NOT NULL,

    PRIMARY KEY (contenu_sk, pays_sk),

    FOREIGN KEY (contenu_sk)
        REFERENCES Fait_Contenu(contenu_sk),

    FOREIGN KEY (pays_sk)
        REFERENCES Dim_Pays(pays_sk)
);
GO

-- Bridge Content Genre
CREATE TABLE Bridge_Contenu_Genre (
    contenu_sk INT NOT NULL,
    genre_sk INT NOT NULL,

    PRIMARY KEY (contenu_sk, genre_sk),

    FOREIGN KEY (contenu_sk)
        REFERENCES Fait_Contenu(contenu_sk),

    FOREIGN KEY (genre_sk)
        REFERENCES Dim_Genre(genre_sk)
);
GO
