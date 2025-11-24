## 📊 Customer Shopping Behavior Analysis

-----

### 🌟 Overview

This is a comprehensive **Data Analytics project** designed to uncover key insights from a customer transactional dataset to inform strategic business decisions. The project demonstrates proficiency in the end-to-end data pipeline, from **data preparation** in Python to **database querying** in SQL, and finally, **visual storytelling** using Power BI.




<img width="4872" height="2656" alt="image" src="https://github.com/user-attachments/assets/47d12909-5e19-4256-bae5-f0e1fb274be8" />



**Key Achievements:**

  * **Data Wrangling:** Cleaned and transformed raw data using Python (Pandas).
  * **Database Management:** Loaded cleaned data into PostgreSQL for structured analysis.
  * **Business Intelligence:** Executed complex SQL queries to answer business questions.
  * **Visualization & Reporting:** Created an interactive Power BI dashboard and final presentation (Gamma).

-----

### 💾 Dataset

The project utilizes the **Customer Shopping Behavior Dataset**, which includes detailed transactional information.

| Metric | Value |
| :--- | :--- |
| **Rows** | 3,900 |
| **Columns** | 17 (after cleaning) |
| **Key Features** | Customer Demographics (Age, Gender, Subscription Status), Purchase Details (Purchase Amount, Category), Shopping Behavior (Review Rating, Frequency) |

-----

### 🛠️ Tools & Technologies

| Category | Tool / Language | Purpose |
| :--- | :--- | :--- |
| **Data Processing** | Python (Pandas, SQLAlchemy) | Data loading, cleaning, transformation, and database connection. |
| **Database** | **PostgreSQL** (Replaceable with MySQL/SQL Server) | Storage and execution of advanced analytical SQL queries. |
| **Visualization** | Power BI | Creating an interactive, dynamic business intelligence dashboard. |
| **Reporting** | Gamma, MS PowerPoint | Final presentation of findings and recommendations. |

-----

### 💻 Analysis Steps

The project was executed in a systematic, multi-stage process:

1.  **Exploratory Data Analysis (EDA) & Cleaning (Python):**
      * Loaded the CSV dataset.
      * Handled missing values in the `Review Rating` column by **imputing the median rating** specific to each product `Category`.
      * Standardized column names to **snake\_case**.
2.  **Feature Engineering (Python):**
      * Created the **`age\_group`** column by binning customer ages using `pd.qcut`.
      * Created **`purchase\_frequency\_days`** by mapping text-based frequencies (e.g., 'Weekly', 'Monthly') to numerical day values.
      * Dropped the redundant **`promo\_code\_used`** column.
3.  **Database Integration & SQL Analysis:**
      * Established a connection to the **PostgreSQL** server using `SQLAlchemy`.
      * Uploaded the final, cleaned DataFrame to a table named `customer`.
      * Executed analytical **SQL queries** to derive business metrics (e.g., highest-spending age group, subscription rate by location, average purchase amount by product category).
4.  **Reporting & Presentation:**
      * Developed a professional **Power BI Dashboard** for visual reporting.
      * Created a final **Report** and a **Presentation** (using Gamma) summarizing the methodology, findings, and strategic recommendations.

-----

### 📈 Results & Business Recommendations

The analysis led to data-driven, actionable recommendations, including:

  * **Boost Subscriptions:** Identified high-potential customer segments for subscription-exclusive promotions.
  * **Customer Loyalty:** Designed a strategy to reward repeat buyers based on purchase frequency.
  * **Targeted Marketing:** Pinpointed the most profitable age groups and shipping preferences for campaign focus.
  * **Product Strategy:** Informed product positioning based on top-rated and best-selling items.

-----

### ⚙️ How to Run

To replicate the project's data preparation and database setup:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/hmurtaza720/Customer_Behavior_Anaylysis.git
    ```
2.  **Prerequisites:**
      * Install **Python 3.x**.
      * Install necessary libraries: `pip install pandas sqlalchemy psycopg2-binary`.
      * Ensure a **PostgreSQL** server is running locally (or adjust the connection string for your chosen database).
3.  **Database Setup:**
      * Create a database named `customer_behavior` in PostgreSQL.
      * **Crucially, update the connection variables** (`password`, `host`, `port`, `database`) in the Python script (`customer_data_pipeline.py` or similar) with your specific credentials.
4.  **Execute Python Script:**
    ```bash
    python customer_data_pipeline.py
    ```
    This script will load, clean, transform the data, and upload the final table to your PostgreSQL database.
5.  **View Results:** The cleaned data will be available in the **`customer`** table in your PostgreSQL database, ready for SQL querying and Power BI connection.


