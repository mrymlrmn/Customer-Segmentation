# Identifying Customer Patterns (RFM Analysis)

## What is this project about?
I took a dataset of over 540,000 retail transactions and tried to answer one big question: **"Who are our customers and how do they shop?"** Instead of looking at 500k rows of raw data, I grouped them into 3 clear categories using the **RFM model** (Recency, Frequency, Monetary). This helps a business know exactly who to reward and who to win back.

## How I did it
* **Data Cleaning:** I cleaned the mess! Handled missing values and removed cancelled orders to make the data reliable.
* **The "Elbow" Trick:** I used the Elbow Method to find the sweet spot for grouping. It turned out that 3 groups were the perfect way to describe this specific customer base.
* **K-Means Clustering:** This is where the machine learning happens. It automatically tagged every customer based on their shopping habits.

## The Results
Here is how we found our 3 types of customers:
1.  **VIPs:** They shop often and spend the most. They are the heart of the business.
2.  **At-Risk:** They used to shop but haven't been back in months. We need to reach out to them.
3.  **Regulars:** They are steady and consistent, but there's room to grow their spending.

![My Elbow Plot](elbow_report.png)

## What's in the files?
* **Business_Strategy_Report.xlsx**: The "Cheat Sheet" for managers. It shows the averages for each group.
* **Final_Customer_Segments.xlsx**: The full list of 540k+ rows with a new "Cluster" column for marketing.

## What I learned
This project taught me how to handle huge Excel files without breaking them and, more importantly, how to turn complex numbers into a simple story that a business owner can understand.

---
**Developed by:** Maryam Larimian  
**Location:** Germany  
**LinkedIn:** [Maryam Larimian](https://www.linkedin.com/in/maryam-larimian)

I built this project to practice data analysis. Currently, I am learning how to turn raw data into simple business reports.