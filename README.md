# 🏙️ NYC Airbnb Listing Performance Analysis under Local Law 18

## 🗂 Repository Outline

This repository contains the files developed for a data engineering and analysis project focusing on the NYC Airbnb market.

1. `description.md`: Overview and documentation of the project (this file).
1. `P2M3_syarief_qayum_ddl.txt`: SQL Data Definition Language (DDL) and Data Manipulation Language (DML) scripts for setting up the PostgreSQL database table and loading raw data.
1. `P2M3_syarief_qayum_data_raw.csv`: The original raw dataset used for the project.
1. `P2M3_syarief_qayum_data_clean.csv`: The dataset after performing cleaning and transformation steps.
1. `P2M3_syarief_qayum_DAG.py`: Apache Airflow Directed Acyclic Graph (DAG) script to automate the data pipeline (Fetch -> Clean -> Load).
1. `P2M3_syarief_qayum_DAG_graph.jpg`: Screenshot of the successful Airflow DAG run graph.
1. `P2M3_syarief_qayum_conceptual.txt`: Answers to conceptual questions regarding NoSQL, Airflow, Great Expectations, and Batch Processing.
1. `P2M3_syarief_qayum_GX.ipynb`: Jupyter Notebook demonstrating data validation using Great Expectations.
1. `/images`: Folder containing screenshots of the Kibana dashboard visualizations and markdown elements.

## 🏘️ Problem Background

The short-term rental market in NYC faces significant pressure from the introduction of local law 18, which began enforcement on September 5, 2023. This law requires mandatory registration and the presence of the host for stays under 30 days. As a result, many listings have disappeared, further impacting the short-term rental market and increasing costs for both hosts and travelers.

This project aims to understand the characteristics of successful Airbnb listings in NYC under these new regulations, providing valuable insights for hosts and property managers to adapt their strategies.

## 🎯 Objective of the Report/Analysis

The goal is to analyze available rental data to identify which types of properties perform best in the current regulatory environment. This includes examining factors such as review ratings, booking numbers, neighborhood, price, and property features.

Based on this analysis, the report will offer actionable recommendations for hosts and property managers, helping them focus on property types and locations that are more likely to succeed under local law 18.

## 📦 Project Output

The main output of this project is an end-to-end data pipeline and analysis that extracts, cleans, validates, and loads Airbnb listing data. The results are visualized and summarized to provide practical recommendations for stakeholders in the NYC short-term rental market.

## 📊 Data

The analysis uses the Airbnb Open Data dataset from Kaggle, which includes details such as listing ID, host information, neighborhood, coordinates, room type, price, service fees, minimum nights, review counts, last review date, review ratings, and house rules. The dataset features a mix of categorical and numerical columns and contains missing values that are addressed during cleaning.

## ⚙️ Method

The project employs an ETL (Extract, Transform, Load) pipeline orchestrated by Apache Airflow for workflow automation and scheduling.

1. **Extract:** Raw data is fetched from a PostgreSQL database (where the original CSV was loaded).
1. **Transform:** Data cleaning is performed using Python and pandas, including removing duplicates, normalizing column names, handling missing values, and converting data types.
1. **Validate:** Data validation is performed using Great Expectations.
1. **Load:** The cleaned data is loaded into a NoSQL database (Elasticsearch).
1. **Visualize & Analyze:** Data is visualized and analyzed using Kibana to generate insights and recommendations.

## 🛠️ Stacks

- **Programming Language:** Python
- **Data Manipulation:** pandas
- **Database Connection:** psycopg2
- **Data Validation:** Great Expectations
- **Workflow Orchestration:** Apache Airflow
- **Source Database:** PostgreSQL (via Docker)
- **Destination Database/Analytics Engine:** Elasticsearch (via Docker)
- **Data Visualization:** Kibana

## Reference
*   **Dataset:** [Airbnb Open Data on Kaggle](http://kaggle.com/datasets/arianazmoudeh/airbnbopendata/data)
*   **NYC Regulation Background:**
    *   [Why Airbnb is welcome in some cities and not in others](https://theconversation.com/why-airbnb-is-welcome-in-some-cities-and-not-in-others-67977)
    *   [Airbnb spent big in NYC mayor's race. It didn't work.](https://www.independent.co.uk/news/world/americas/us-politics/airbnb-super-pac-nyc-mayor-b2767428.html)
    *   [NYC sees record rents, hotel rates as short-term rental law continues](https://news.airbnb.com/nyc-sees-record-rents-hotel-rates-as-short-term-rental-law-continues/?utm_source=google&utm_medium=cpc&utm_campaign=se-bnb21-se-trfc-us-srch-en-search-SPM-40E8057F&c=.pi0.pk21839625089_178512513006&gad_source=1&gad_campaignid=21839625089&gbraid=0AAAAADQe07eiGdjXcc2wfsZdsofh1WkEY&gclid=CjwKCAjwsZPDBhBWEiwADuO6y8ippRjhVaFBKj2JpMzvdmckmVItJojn9m6v3Bgtp3vaeWjH_ewhJhoCvOoQAvD_BwE)
*   **Kibana Dashboard:** *(screenshot in the /images folder)*

---
