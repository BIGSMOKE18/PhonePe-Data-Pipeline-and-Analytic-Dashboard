# 📊 PhonePe Data Engineering Pipeline & Analytics Dashboard

## 🚀 Project Overview

This project implements an end-to-end **Data Engineering pipeline** to process and analyze PhonePe transaction data across India. The pipeline ingests raw JSON data, transforms it into a structured format, stores it in a database, and generates business insights through SQL queries and dashboards.

---

## 🎯 Objectives

* Build a scalable ETL pipeline for multi-year transaction data
* Convert nested JSON data into structured tabular format
* Perform data cleaning and validation
* Store processed data in SQL database
* Generate insights and visualize trends using dashboards

---

## 🏗️ Architecture

```
Raw JSON Data → Python (Ingestion & Transformation) → Pandas (Cleaning) → SQL (Storage & Querying) → Tableau/Power BI (Visualization)
```

---

## 🧰 Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, JSON, OS
* **Database:** SQLite
* **Visualization:** Tableau / Power BI
* **Concepts:** ETL Pipeline, Data Cleaning, Data Modeling

---

## 📂 Dataset

* Source: PhonePe Pulse Dataset (public dataset from PhonePe)
* Data includes:

  * State-wise transactions
  * Year-wise and quarter-wise trends
  * Category-wise transaction details

---

## ⚙️ Pipeline Workflow

### 1. Data Ingestion

* Extracted JSON files for all states, years (2018–2024), and quarters
* Automated file traversal using Python

### 2. Data Transformation

* Parsed nested JSON structure
* Extracted key fields: State, Year, Quarter, Category, Count, Amount

### 3. Data Cleaning

* Handled missing values
* Removed duplicates
* Standardized column names and formats

### 4. Data Storage

* Loaded cleaned data into SQLite database
* Created structured table for efficient querying

### 5. Data Analysis

* Used SQL queries to identify:

  * Top states by transaction amount
  * Category-wise distribution
  * Year-wise growth trends

### 6. Data Visualization

* Built interactive dashboards showing:

  * Top-performing states
  * Category contribution
  * Growth over time

---

## 📊 Key Insights

* Identified top-performing states based on transaction volume
* Observed dominant transaction categories (e.g., P2P, Merchant Payments)
* Analyzed growth trends across years and quarters

---


---

## ▶️ How to Run

1. Clone the repository

```
git clone <your-repo-link>
```

2. Install dependencies

```
pip install pandas
```

3. Run the pipeline

```
python read_json.py
```

4. Output:

* Cleaned dataset (CSV)
* SQLite database with transactions table

---

## 🧠 Learning Outcomes

* Built real-world ETL pipeline
* Worked with nested JSON data
* Gained experience in SQL-based data analysis
* Developed dashboard for business insights

---

## 📌 Future Improvements

* Integrate cloud services (Azure Data Factory / AWS)
* Implement real-time data ingestion
* Add advanced analytics and forecasting

---

## 👨‍💻 Author

Ayush Dhar
Final Year IT Engineering Student

---
