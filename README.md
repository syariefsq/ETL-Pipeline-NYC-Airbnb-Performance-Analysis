# NYC Airbnb Listing Performance Analysis under Local Law 18

## Repository Outline
This repository contains the files developed for a data engineering and analysis project focusing on the NYC Airbnb market.

1.  `description.md`: Overview and documentation of the project (this file).
2.  `P2M3_syarief_qayum_ddl.txt`: SQL Data Definition Language (DDL) and Data Manipulation Language (DML) scripts for setting up the PostgreSQL database table and loading raw data.
3.  `P2M3_syarief_qayum_data_raw.csv`: The original raw dataset used for the project.
4.  `P2M3_syarief_qayum_data_clean.csv`: The dataset after performing cleaning and transformation steps.
5.  `P2M3_syarief_qayum_DAG.py`: Apache Airflow Directed Acyclic Graph (DAG) script to automate the data pipeline (Fetch -> Clean -> Load).
6.  `P2M3_syarief_qayum_DAG_graph.jpg`: Screenshot of the successful Airflow DAG run graph.
7.  `P2M3_syarief_qayum_conceptual.txt`: Answers to conceptual questions regarding NoSQL, Airflow, Great Expectations, and Batch Processing.
8.  `P2M3_syarief_qayum_GX.ipynb`: Jupyter Notebook demonstrating data validation using Great Expectations.
9.  `/images`: Folder containing screenshots of the Kibana dashboard visualizations and markdown elements.

## Problem Background
The short-term rental market in NYC faces significant pressure from newly established local law 18 (This law impose started since Sep 5, 2023) which impose the mandatory registration and host must be present for stays in Rent under 30 Days. (Other cities anyone can rent out their places regardless). Because of that many listings have disappear and impacted short term rental making NYC even more expensive for host and travelers.

We will try to understand successful listings in this context which will be beneficial for hosts and property managers to layout the strategies for this challenge.

## Objective of the Report/Analysis:

As data scientist we will analyze the information from existing different rentals in NYC from the dataset and looks closely at the characteristics of properties that perform better than others (data such as review stars, booking numbers) and connecting with the are such as neighbourhoods of the property and numerical information such as costs and property details (type of property, number of rooms)

Base on those information, we will create report and recommendations both for individual host and property managers to focus on certain types of properties/rentals by locations and what characteristics of good properties based on their performance. (Even with the challenge of the local law 18)

## Project Output
The primary output of this project is to evaluate understanding and application of data engineering and analysis tools and concepts learned in Phase 2, including **Apache Airflow, Great Expectations, NoSQL databases (Elasticsearch), and data visualization with Kibana**. The main task is to build a data pipeline that extracting data from PostgreSQL, cleans and validates it, and loads it into Elasticsearch for visualization using Kibana.

## Data
The project utilizes the **Airbnb Open Data dataset** sourced from Kaggle. This dataset contains detailed information about Airbnb listings in NYC, including listing ID, host details, neighbourhood, geographical coordinates, room type, price, service fees, minimum nights, number of reviews, last review date, review ratings, and house rules. The dataset includes a mix of categorical and numerical columns and contains missing values that require handling.

## Method
The project employs an ETL (Extract, Transform, Load) pipeline orchestrated by Apache Airflow for workflow automation and scheduling.
1.  **Extract:** Raw data is fetched from a PostgreSQL database (where the original CSV was loaded).
2.  **Transform:** Data cleaning is performed using Python and pandas, including removing duplicates, normalizing column names (lowercase, underscores), handling missing values (filling with placeholders or zeros), and converting data types (e.g., price from string to numeric).
3.  **Validate:** Perform data validation on the cleaned using Great Expectations.
4.  **Load:** Prepare data for and load into a NoSQL database (Elasticsearch).
5.  **Visualize & Analyze:** Process and visualize data using Kibana to create an analytical report.

## Stacks
*   **Programming Language:** Python
*   **Data Manipulation:** pandas
*   **Database Connection:** psycopg2
*   **Data Validation:** Great Expectations
*   **Workflow Orchestration:** Apache Airflow
*   **Source Database:** PostgreSQL (via Docker)
*   **Destination Database/Analytics Engine:** Elasticsearch (via Docker)
*   **Data Visualization:** Kibana

## Reference
*   **Dataset:** [Airbnb Open Data on Kaggle](http://kaggle.com/datasets/arianazmoudeh/airbnbopendata/data)
*   **NYC Regulation Background:**
    *   [Why Airbnb is welcome in some cities and not in others](https://theconversation.com/why-airbnb-is-welcome-in-some-cities-and-not-in-others-67977)
    *   [Airbnb spent big in NYC mayor's race. It didn't work.](https://www.independent.co.uk/news/world/americas/us-politics/airbnb-super-pac-nyc-mayor-b2767428.html)
    *   [NYC sees record rents, hotel rates as short-term rental law continues](https://news.airbnb.com/nyc-sees-record-rents-hotel-rates-as-short-term-rental-law-continues/?utm_source=google&utm_medium=cpc&utm_campaign=se-bnb21-se-trfc-us-srch-en-search-SPM-40E8057F&c=.pi0.pk21839625089_178512513006&gad_source=1&gad_campaignid=21839625089&gbraid=0AAAAADQe07eiGdjXcc2wfsZdsofh1WkEY&gclid=CjwKCAjwsZPDBhBWEiwADuO6y8ippRjhVaFBKj2JpMzvdmckmVItJojn9m6v3Bgtp3vaeWjH_ewhJhoCvOoQAvD_BwE)
*   **Kibana Dashboard:** *(screenshot in the /images folder)*

---