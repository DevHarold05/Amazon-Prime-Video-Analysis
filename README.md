# 🎬 Amazon Prime Video – Data Analysis Project

[🔗![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[🔗![SQL Server](https://img.shields.io/badge/SQL_Server-Database-red?logo=microsoftsqlserver)](https://www.microsoft.com/en-us/sql-server)
[🔗![Power BI](https://img.shields.io/badge/Power_BI-Data_Visualization-yellow?logo=powerbi)](https://powerbi.microsoft.com/)
[🔗![Dataset](https://img.shields.io/badge/Dataset-Amazon_Prime_Video-blue?logo=kaggle)](https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows?resource=download)
## 📌 1. Project Overview

This project focuses on analyzing the **Amazon Prime Video content catalogue** using a complete data analysis and Business Intelligence workflow.

The main objective is to transform raw data into meaningful insights through several stages, starting with data preparation in Python, followed by data integration and Data Warehouse development using SQL Server, and finally interactive visualization with Power BI.

The analysis explores the structure and distribution of movies and TV shows available in the catalogue. It aims to identify content trends, understand the geographical distribution of productions, discover the most represented genres, and examine the evolution of content over the years.

Through this project, I applied practical skills in **Data Cleaning, Exploratory Data Analysis (EDA), SQL, Dimensional Modeling, Data Warehousing, DAX, and Data Visualization**.

🎯 **Main Goals:**
- Understand the structure and quality of the dataset.
- Clean and prepare raw data for analysis.
- Explore content distribution and identify significant trends.
- Build a structured Data Warehouse.
- Design an interactive Power BI dashboard.
- Transform raw data into clear and useful business insights.

## 🛠️ 2. Technologies & Tools

| Technology | Purpose |
|---|---|
| 🐍 Python | Data Cleaning and Exploratory Data Analysis |
| 🐼 Pandas | Data manipulation and preparation |
| 📊 Matplotlib & Seaborn | Data visualization |
| 🗄️ SQL Server | Data storage and management |
| ⭐ Data Warehouse | Dimensional modeling and data integration |
| 📈 Power BI | Interactive dashboards and reporting |
| 🧮 DAX | Calculations and analytical measures |

## 📂 3. Project Workflow

### 🔹 Step 1 – Data Cleaning with Python
- Loading the raw dataset.
- Exploring columns, data types and missing values.
- Handling missing and inconsistent values.
- Checking duplicates and abnormal values.
- Preparing a clean dataset for analysis.

### 🔹 Step 2 – Exploratory Data Analysis (EDA)
- Analyzing movies versus TV shows.
- Studying content distribution by country.
- Identifying the most popular catalogue genres by representation.
- Exploring content ratings.
- Analyzing release-year trends.
- Creating visualizations to understand the dataset.

### 🔹 Step 3 – SQL Server Integration
- Creating the source database.
- Importing the cleaned dataset into SQL Server.
- Creating and validating staging tables.
- Checking record counts and data consistency.

### 🔹 Step 4 – Data Warehouse Development
- Creating a separate Data Warehouse database.
- Designing a dimensional model.
- Creating dimension tables and a central fact table.
- Creating bridge tables to manage multiple countries and genres per content.
- Loading and validating data using SQL queries.

### 🔹 Step 5 – Power BI Dashboard
- Connecting Power BI to the Data Warehouse.
- Creating relationships between tables.
- Developing analytical measures using DAX.
- Designing interactive charts and visualizations.
- Building a dashboard to explore the Prime Video catalogue.

## 📊 4. Key Performance Indicators (KPIs)

The dashboard includes indicators such as:

- 🎬 Total number of contents.
- 🎥 Total number of movies.
- 📺 Total number of TV shows.
- 🌍 Number of represented countries.
- 🎭 Number of represented genres.
- 📊 Percentage of movies and TV shows.

## 📈 5. Dashboard Analysis

The Power BI dashboard provides insights into:

- **Content Type:** Distribution of movies and TV shows.
- **Release Year:** Evolution of catalogue content by release year.
- **Countries:** Top 10 countries by number of associated contents.
- **Genres:** Most represented genres.
- **Age Ratings:** Distribution of content according to age classification.
- **Movies vs TV Shows:** Comparison of content types over time.

## 🗄️ 6. Data Warehouse Model

The Data Warehouse is organized around a central fact table:

**Fact Table:**
- `Fait_Contenu`

**Dimension Tables:**
- `Dim_Type`
- `Dim_Rating`
- `Dim_AnneeSortie`
- `Dim_Pays`
- `Dim_Genre`

**Bridge Tables:**
- `Bridge_Contenu_Pays`
- `Bridge_Contenu_Genre`

The bridge tables handle many-to-many relationships between content and countries, and between content and genres.

## 📦 7. Dataset

The project uses a publicly available Amazon Prime Video catalogue dataset.

The dataset contains information such as:
- Content ID
- Title
- Content type
- Director
- Cast
- Country
- Date added
- Release year
- Age rating
- Duration
- Genres
- Description

**Note:** This project analyzes catalogue metadata. It does not measure actual views, subscriptions, revenue, or customer behavior.

