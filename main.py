from src.data_loader import Cus_Segment_DataLoader
from src.preprocessing import Cus_Segment_Preprocessor
from src.model_trainer import Cus_Segment_Model
import pandas as pd

def run(file_path=None):
    loader = Cus_Segment_DataLoader()
    raw_data = loader.data_loader(file_path)

    preprocessor = Cus_Segment_Preprocessor()
    scaled_data, clean_customer_df = preprocessor.process(raw_data)

    trainer = Cus_Segment_Model(n_clusters=3)
    clean_customer_df['Cluster'] = trainer.train(scaled_data)

    cluster_means = clean_customer_df.groupby('Cluster')[['Total_Spent', 'Frequency', 'Recency']].mean()
    labels = {}
    for cluster in cluster_means.index:
        if cluster_means.loc[cluster, 'Total_Spent'] == cluster_means['Total_Spent'].max():
            labels[cluster] = 'VIP'
        elif cluster_means.loc[cluster, 'Recency'] == cluster_means['Recency'].max():
            labels[cluster] = 'At-Risk'
        else:
            labels[cluster] = 'Regular'
    clean_customer_df['Segment'] = clean_customer_df['Cluster'].map(labels)

    return clean_customer_df

if __name__ == "__main__":
    df = run()
    df.to_excel("data/Final_Customer_Segments.xlsx", index=False)
    print("Project execution completed successfully!")