# Customer Segmentation with K-Means Clustering

I started this project with a simple question: if you have half a million transactions, how do you actually make sense of them?

The dataset is from an online retail store — 540,000+ rows of raw sales data. Instead of drowning in numbers, I used the RFM model (Recency, Frequency, Monetary) to group customers into 3 meaningful segments. The kind of insight a marketing team can actually use.

## How it works

First I had to clean the data quite a bit. There were missing customer IDs, cancelled orders mixed in with real ones, and general messiness you'd expect from real-world retail data. Once that was sorted, I calculated RFM scores for each customer — basically: when did they last buy, how often do they buy, and how much do they spend?

Then came the interesting part. I used the Elbow Method to figure out the right number of clusters — turned out 3 was the sweet spot for this dataset. K-Means did the rest.

## What the clusters look like

![Elbow Plot](elbow_report.png)

After running the model, three types of customers emerged:

- **VIPs** — shop frequently, spend the most, came back recently. The backbone of the business.
- **At-Risk** — used to be good customers but haven't shown up in a while. Worth a targeted campaign.
- **Regulars** — consistent but not big spenders. Room to grow.

## Output files

- `Final_Online Retail.xlsx` — the full dataset with a Cluster column added to each row
- `Business_Strategy_Report.xlsx` — a summary table with averages per segment, written for non-technical readers

## Tech stack

- Python
- Pandas, Scikit-Learn
- Matplotlib, Seaborn, OpenPyXL

## How to run

```
pip install -r requirements.txt
python main.py
```

## What I'd do next

I'd like to add a simple dashboard — maybe with Streamlit — so the results are visual and interactive instead of just sitting in an Excel file.

---

*Dataset: Online Retail — UCI Machine Learning Repository via Kaggle*  
*Developed by Maryam Larimian — Germany*
