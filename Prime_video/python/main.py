import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Indiquez le chemin vers votre fichier CSV (par exemple sur votre clé USB ou dossier)
# Remplacez le chemin par l'emplacement réel de votre fichier
chemin_fichier = "D:/Prime_video/amazon_prime_titles.csv" 

# Charger le dataset
df = pd.read_csv(chemin_fichier)

# 1. Afficher les premières lignes pour voir à quoi ressemblent les données
print("--- Premières lignes ---")
print(df.head(3))

# 2. Afficher la structure globale (nombre de lignes, colonnes, types de données)
print("\n--- Informations générales (Structure) ---")
df.info()

# 3. Lister le nom de toutes les colonnes disponibles
print("\n--- Liste des colonnes ---")
print(df.columns.tolist())

# 4. Dimensions du dataset
print("\n--- Dimensions ---")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

# 5. Types de données
print("\n--- Types de données ---")
print(df.dtypes)

# 6. Statistiques descriptives
print("\n--- Statistiques descriptives ---")
print(df.describe(include="all"))

# 7. Valeurs manquantes
print("\n--- VALEURS MANQUANTES ---")

missing = pd.DataFrame({
    "Nombre_manquant": df.isnull().sum(),
    "Pourcentage": (df.isnull().mean() * 100).round(2)
})

print(missing.sort_values(by="Pourcentage", ascending=False))

# 8. Doublons
print("\n--- DOUBLONS ---")

print("Doublons complets :", df.duplicated().sum())

print("Identifiants dupliqués :", df["show_id"].duplicated().sum())

print("Titres dupliqués :", df["title"].duplicated().sum())

# 9. Types de contenu
print("\n--- TYPES DE CONTENU ---")

print(df["type"].value_counts())

print("\nPourcentage :")

print((df["type"].value_counts(normalize=True) * 100).round(2))

# 10. Années de sortie
print("\n--- ANNÉES DE SORTIE ---")

print(df["release_year"].describe())

print("\nTop 10 des années :")

print(df["release_year"].value_counts().head(10))

# 11. Durée des films et séries
print("\n--- DURÉES ---")

print(df["duration"].value_counts().head(15))
# 13. Séparer les pays
pays = df["country"].dropna().str.split(", ").explode()

# 14. Compter les contenus par pays
top_pays = pays.value_counts().head(10)

print("--- TOP 10 DES PAYS ---")
print(top_pays)



genres = df["listed_in"].dropna().str.split(", ").explode()

top_genres = genres.value_counts().head(10)

print("--- TOP 10 DES GENRES ---")
print(top_genres)


contenus_annee = df["release_year"].value_counts().sort_index()


# Créer une copie pour conserver les données originales
df_clean = df.copy()

# Remplacer les valeurs manquantes par une indication
colonnes = ["director", "cast", "country", "rating"]

for col in colonnes:
    df_clean[col] = df_clean[col].fillna("Unknown")

# Vérification
print(df_clean.isnull().sum())

df_clean["date_added"] = pd.to_datetime(
    df_clean["date_added"],
    errors="coerce"
)

print(df_clean["date_added"].dtype)

df_clean["duration_value"] = pd.to_numeric(
    df_clean["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

df_clean["duration_unit"] = df_clean["duration"].str.extract(
    r"([A-Za-z]+)"
)

print(df_clean[["duration", "duration_value", "duration_unit"]].head(10))

print("Dimensions avant :", df.shape)
print("Dimensions après :", df_clean.shape)

print("\nValeurs manquantes après nettoyage :")
print(df_clean.isnull().sum())

print("=== TYPES DE CONTENU ===")
print(df_clean["type"].value_counts())

print("\n=== UNITÉS DE DURÉE ===")
print(df_clean["duration_unit"].value_counts())

print("\n=== CLASSIFICATIONS ===")
print(df_clean["rating"].value_counts())

print("\n=== ANNÉES DE SORTIE ===")
print("Année minimale :", df_clean["release_year"].min())
print("Année maximale :", df_clean["release_year"].max())

print("\n=== VALEURS MANQUANTES ===")
print(df_clean.isnull().sum())

df_clean.to_csv(
    "D:/Prime_video/amazon_prime_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Fichier nettoyé enregistré avec succès !")

# Nombre de films et de séries
repartition = df_clean["type"].value_counts()

# Pourcentage de chaque type
pourcentage = df_clean["type"].value_counts(normalize=True) * 100

# Regrouper les résultats dans un tableau
analyse_type = pd.DataFrame({
    "Nombre": repartition,
    "Pourcentage": pourcentage.round(2)
})

print(analyse_type)


# Nombre de contenus par année de sortie
contenus_par_annee = (
    df_clean.groupby("release_year")
    .size()
    .sort_values(ascending=False)
)

print("Les 10 années les plus représentées :")
print(contenus_par_annee.head(10))

# Visualisation de l'évolution du nombre de contenus par année de sortie
contenus_par_annee = df_clean["release_year"].value_counts().sort_index()

plt.figure(figsize=(12, 5))



# Regrouper les contenus par année et par type
evolution_type = df_clean.groupby(
    ["release_year", "type"]
).size().unstack(fill_value=0)

print(evolution_type.tail(15))

evolution_type = df_clean.groupby(
    ["release_year", "type"]
).size().unstack(fill_value=0)


# Créer une copie des données avec les pays connus uniquement
pays = df_clean[df_clean["country"] != "Unknown"].copy()

# Séparer les pays multiples
pays["country"] = pays["country"].str.split(", ")

# Transformer chaque pays en ligne individuelle
pays = pays.explode("country")

# Compter les contenus par pays
top_pays = pays["country"].value_counts().head(10)

print("Les 10 pays les plus représentés :")
print(top_pays)



# Séparer les genres multiples
genres = df_clean.copy()

genres["listed_in"] = genres["listed_in"].str.split(", ")

# Transformer chaque genre en ligne individuelle
genres = genres.explode("listed_in")

# Compter les occurrences de chaque genre
top_genres = genres["listed_in"].value_counts().head(10)

print("Les 10 genres les plus représentés :")
print(top_genres)

# Sélectionner uniquement les films
films = df_clean[df_clean["type"] == "Movie"]

# Statistiques descriptives de leur durée
print("=== DURÉE DES FILMS ===")
print(films["duration_value"].describe())

# Sélectionner uniquement les séries
series = df_clean[df_clean["type"] == "TV Show"]

# Statistiques descriptives du nombre de saisons
print("=== NOMBRE DE SAISONS DES SÉRIES ===")
print(series["duration_value"].describe())

# Films avec une durée nulle
print("=== FILMS AVEC UNE DURÉE NULLE ===")

print(
    films[films["duration_value"] == 0][
        ["title", "duration", "duration_value"]
    ]
)

# Films avec une durée supérieure à 300 minutes
print("\n=== FILMS DE PLUS DE 300 MINUTES ===")

print(
    films[films["duration_value"] > 300][
        ["title", "duration", "duration_value"]
    ]
)

# Créer une copie des films pour l'analyse
films_analyse = films[films["duration_value"] > 0].copy()

# Statistiques après exclusion des durées nulles
print("Nombre de films avant traitement :", len(films))

print("Nombre de films après traitement :", len(films_analyse))

print("\n=== NOUVELLES STATISTIQUES ===")
print(films_analyse["duration_value"].describe())

#-----------------------------------------------#
# ================== TOUS LES GRAPHIQUES DANS UNE SEULE FENÊTRE ==================
fig, axes = plt.subplots(3, 3, figsize=(22, 14))
fig.suptitle("Analyse du catalogue Amazon Prime Video", fontsize=20, fontweight="bold")

# 1. Répartition films / séries
sns.countplot(data=df_clean, x="type", ax=axes[0, 0])
axes[0, 0].set_title("Répartition des films et séries")
axes[0, 0].set_xlabel("Type de contenu")
axes[0, 0].set_ylabel("Nombre de contenus")

# 2. Top 10 des pays
sns.barplot(x=top_pays.values, y=top_pays.index, ax=axes[0, 1])
axes[0, 1].set_title("Top 10 des pays")
axes[0, 1].set_xlabel("Nombre de contenus")
axes[0, 1].set_ylabel("Pays")

# 3. Top 10 des genres
sns.barplot(x=top_genres.values, y=top_genres.index, ax=axes[0, 2])
axes[0, 2].set_title("Top 10 des genres")
axes[0, 2].set_xlabel("Nombre de contenus")
axes[0, 2].set_ylabel("Genre")

# 4. Évolution du nombre de contenus par année
contenus_par_annee = df_clean["release_year"].value_counts().sort_index()
axes[1, 0].plot(contenus_par_annee.index, contenus_par_annee.values, marker="o", markersize=3)
axes[1, 0].set_title("Évolution des contenus par année de sortie")
axes[1, 0].set_xlabel("Année de sortie")
axes[1, 0].set_ylabel("Nombre de contenus")
axes[1, 0].grid(True)

# 5. Films vs séries par année
evolution_type = df_clean.groupby(["release_year", "type"]).size().unstack(fill_value=0)
axes[1, 1].plot(evolution_type.index, evolution_type["Movie"], marker="o", markersize=3, label="Movies")
axes[1, 1].plot(evolution_type.index, evolution_type["TV Show"], marker="o", markersize=3, label="TV Shows")
axes[1, 1].set_title("Évolution des films et séries par année")
axes[1, 1].set_xlabel("Année de sortie")
axes[1, 1].set_ylabel("Nombre de contenus")
axes[1, 1].legend()
axes[1, 1].grid(True)

# 6. Distribution de la durée des films
sns.histplot(data=films_analyse, x="duration_value", bins=30, kde=True, ax=axes[1, 2])
axes[1, 2].set_title("Distribution de la durée des films")
axes[1, 2].set_xlabel("Durée (minutes)")
axes[1, 2].set_ylabel("Nombre de films")

# 7. Distribution du nombre de saisons
sns.countplot(data=series, x="duration_value", ax=axes[2, 0])
axes[2, 0].set_title("Distribution du nombre de saisons")
axes[2, 0].set_xlabel("Nombre de saisons")
axes[2, 0].set_ylabel("Nombre de séries")

# Cases vides : on les masque
axes[2, 1].axis("off")
axes[2, 2].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

