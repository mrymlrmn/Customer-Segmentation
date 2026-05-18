# Customer Segmentation with K-Means Clustering

I started this project with a simple question: if you have half a million transactions, how do you actually make sense of them? The goal was simple: can a machine learning model learn these patterns and make reasonable predictions?

**[Try the live app here](https://customer-segmentation-igjuvrtuezbbbjkt2hmytw.streamlit.app/)**

## What I did

I took a dataset of an online retail store — over 540,000 rows of raw transactions — and built a K-Means clustering pipeline from scratch. Instead of throwing everything into one script, I split the code into separate modules — data loading, cleaning, feature engineering, and model training. Keeping things modular made it easier to debug and actually understand what each part was doing.

I also built a small web app with Streamlit so anyone can enter their details and get a cost estimate instantly — no code required.

## Results

After using the Elbow Method to find the right number of clusters, 3 turned out to be the sweet spot for this dataset. K-Means did the rest, and three distinct customer personas emerged:

- **VIPs** — shop frequently, spend the most, came back recently. The backbone of the business.
- **At-Risk** — used to be good customers but haven't shown up in a while. Worth a targeted campaign.
- **Regulars** — consistent but not big spenders. Room to grow.

The project automatically outputs structured Excel files (like `Business_Strategy_Report.xlsx`) that summarize these segments with clear metrics for non-technical managers.

## Tech Stack

- Python
- Pandas, Scikit-Learn
- Matplotlib, Seaborn
- OpenPyXL (for Excel report generation)
- Streamlit (for the web app)

## How to run it

pip install -r requirements.txt
python main.py
streamlit run app.py

## What I'd do differently next time

K-Means is great for a snapshot, but customer behavior changes over time. I'd like to try tracking these clusters dynamically over months to see how customers drift between segments — especially since watching a VIP turn into an At-Risk customer in real-time adds way more value.

---

*Dataset from Kaggle — Online Retail Dataset (UCI Machine Learning Repository)*

---
**Developed by:** Maryam Lraimian


