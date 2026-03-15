# Global Climate Disaster Analysis (2000–2023)

This project explores global natural disaster data to understand how disasters evolve over time, where they occur most frequently, and what types of disasters cause the greatest human and economic impact.

The analysis was built as a complete end-to-end data analytics workflow starting from raw disaster records and ending with an interactive Power BI dashboard designed to support exploratory analysis and data storytelling.

---

## Project Objective

Natural disasters continue to increase in frequency and intensity due to climate change and environmental factors. Understanding their patterns is essential for governments, researchers, and policy makers.

This project aims to answer several key questions:

- How have global disasters evolved over time?
- Which countries and regions are most affected?
- Which disaster types cause the most damage and fatalities?
- What global patterns can be observed from historical disaster data?

---

## Data Source

The dataset used in this project comes from the **EM-DAT International Disaster Database**, which provides global records of natural disasters including their location, type, casualties, and economic losses.

The raw dataset required preprocessing before it could be analyzed effectively.

---

## Data Processing Pipeline

The project follows a structured analytics pipeline:

Raw Disaster Dataset  
→ Data Cleaning & Preparation (Python)  
→ Database Storage (MySQL)  
→ Analytical Queries (SQL)  
→ Interactive Visualization (Power BI)

Each stage was designed to simulate a real-world analytics workflow used in data teams.

---

## Data Cleaning

Initial data preparation was performed using **Python and Pandas**.

Key steps included:
- selecting relevant analytical columns
- standardizing column names
- handling missing values
- converting data types
- preparing the dataset for database storage

The cleaned dataset was then exported and prepared for database ingestion.

---

## Database Design

The cleaned dataset was imported into a **MySQL database** to enable structured querying and efficient analysis.

Main table used in the project:

`disasters`

Important fields include:

- disaster_id  
- country  
- region  
- disaster_type  
- disaster_subtype  
- year  
- total_deaths  
- total_damage_usd  

Storing the data in a database allows complex aggregations and analytical queries to be executed efficiently.

---

## SQL Analysis

A set of analytical SQL queries were written to explore patterns in the data.

Examples of analyses performed include:

- disaster frequency trends over time
- most affected countries
- disaster distribution by type
- economic damage by disaster type
- fatalities caused by different disasters

These queries serve as the analytical foundation for the final dashboard.

---

## Dashboard Development

The final stage of the project is an interactive **Power BI dashboard** designed to communicate insights clearly and allow users to explore the data dynamically.

The dashboard includes:

- Global disaster overview (KPI metrics)
- Disaster trends over time
- Top 10 most affected countries
- Disaster type distribution
- Economic losses by disaster type
- Fatalities by disaster type
- Geographic distribution of disasters
- Interactive filters by year, region, and disaster type

The dashboard enables users to quickly identify patterns and understand the global impact of natural disasters.

---

## Key Insights

Several patterns emerge from the analysis:

Floods represent the most frequent disaster type globally, while storms generate the highest economic losses.  
Earthquakes, although less frequent, account for the highest number of fatalities.  
Asia experiences the highest concentration of disaster events, highlighting the region's vulnerability to natural hazards.  
The overall number of disaster events shows an increasing trend during the early 2000s before stabilizing in recent years.

---

# Global Climate Disaster Analysis (2000–2023)

This project explores global natural disaster data to understand how disasters evolve over time, where they occur most frequently, and what types of disasters cause the greatest human and economic impact.

The analysis was built as a complete end-to-end data analytics workflow starting from raw disaster records and ending with an interactive Power BI dashboard designed to support exploratory analysis and data storytelling.

---

## Project Objective

Natural disasters continue to increase in frequency and intensity due to climate change and environmental factors. Understanding their patterns is essential for governments, researchers, and policy makers.

This project aims to answer several key questions:

- How have global disasters evolved over time?
- Which countries and regions are most affected?
- Which disaster types cause the most damage and fatalities?
- What global patterns can be observed from historical disaster data?

---

## Data Source

The dataset used in this project comes from the **EM-DAT International Disaster Database**, which provides global records of natural disasters including their location, type, casualties, and economic losses.

The raw dataset required preprocessing before it could be analyzed effectively.

---

## Data Processing Pipeline

The project follows a structured analytics pipeline:

Raw Disaster Dataset  
→ Data Cleaning & Preparation (Python)  
→ Database Storage (MySQL)  
→ Analytical Queries (SQL)  
→ Interactive Visualization (Power BI)

Each stage was designed to simulate a real-world analytics workflow used in data teams.

---

## Data Cleaning

Initial data preparation was performed using **Python and Pandas**.

Key steps included:
- selecting relevant analytical columns
- standardizing column names
- handling missing values
- converting data types
- preparing the dataset for database storage

The cleaned dataset was then exported and prepared for database ingestion.

---

## Database Design

The cleaned dataset was imported into a **MySQL database** to enable structured querying and efficient analysis.

Main table used in the project:

`disasters`

Important fields include:

- disaster_id  
- country  
- region  
- disaster_type  
- disaster_subtype  
- year  
- total_deaths  
- total_damage_usd  

Storing the data in a database allows complex aggregations and analytical queries to be executed efficiently.

---

## SQL Analysis

A set of analytical SQL queries were written to explore patterns in the data.

Examples of analyses performed include:

- disaster frequency trends over time
- most affected countries
- disaster distribution by type
- economic damage by disaster type
- fatalities caused by different disasters

These queries serve as the analytical foundation for the final dashboard.

---

## Dashboard Development

The final stage of the project is an interactive **Power BI dashboard** designed to communicate insights clearly and allow users to explore the data dynamically.

The dashboard includes:

- Global disaster overview (KPI metrics)
- Disaster trends over time
- Top 10 most affected countries
- Disaster type distribution
- Economic losses by disaster type
- Fatalities by disaster type
- Geographic distribution of disasters
- Interactive filters by year, region, and disaster type

The dashboard enables users to quickly identify patterns and understand the global impact of natural disasters.

---

## Key Insights

Several patterns emerge from the analysis:

Floods represent the most frequent disaster type globally, while storms generate the highest economic losses.  
Earthquakes, although less frequent, account for the highest number of fatalities.  
Asia experiences the highest concentration of disaster events, highlighting the region's vulnerability to natural hazards.  
The overall number of disaster events shows an increasing trend during the early 2000s before stabilizing in recent years.

---

## Technologies Used

Python (Pandas)  
MySQL  
SQL  
Power BI

---

## Author

Najwa Zhafarina Alyani Wilujeng

