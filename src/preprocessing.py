import pandas as pd
from sklearn.preprocessing import StandardScaler

class Cus_Segment_Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def process(self, df: pd.DataFrame):
        # 1. Clean data
        df = df.dropna(subset=['CustomerID'])
        df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
        df['Total_Spent'] = df['Quantity'] * df['UnitPrice']

        # 2. Aggregation (Grouping by Customer)
        customer_df = df.groupby('CustomerID').agg({
            'Total_Spent': 'sum',      # Monetary
            'InvoiceNo': 'count',     # Frequency
            'InvoiceDate': 'max'      # For Recency
        }).reset_index()

        # 3. Calculate Recency (Days since last purchase)
        snapshot_date = customer_df['InvoiceDate'].max() + pd.Timedelta(days=1)
        customer_df['Recency'] = (snapshot_date - customer_df['InvoiceDate']).dt.days

        # 4. Rename columns (MATCHING NAMES START HERE)
        customer_df.columns = ['CustomerID', 'Total_Spent', 'Frequency', 'Last_Purchase_Date', 'Recency']

        # 5. Select features for the AI model
        features = ['Total_Spent', 'Frequency', 'Recency']
        scaled_data = self.scaler.fit_transform(customer_df[features])

        return scaled_data, customer_df