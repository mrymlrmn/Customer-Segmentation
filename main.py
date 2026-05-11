from src.data_loader import Cus_Segment_DataLoader
from src.preprocessing import Cus_Segment_Preprocessor
from src.visualizer import Cus_Segment_Visualizer
from src.model_trainer import Cus_Segment_Model  # New import
import pandas as pd

def main():
    # 1. Data Loading
    loader = Cus_Segment_DataLoader()
    raw_data = loader.data_loader("data/Mall_Customers.xlsx") 

    # 2. Preprocessing
    preprocessor = Cus_Segment_Preprocessor()
    scaled_data, clean_customer_df = preprocessor.process(raw_data)

    # 3. Visualization (Optional: you can comment this out after finding k)
    # visualizer = Cus_Segment_Visualizer()
    # visualizer.plot_elbow_method(scaled_data)

    # 4. Model Training (Using our new trainer class)
    print("--- Training the Model ---")
    trainer = Cus_Segment_Model(n_clusters=3) # We chose 3 from the elbow plot
    clean_customer_df['Cluster'] = trainer.train(scaled_data)

    # 5. Analysis
    print("\n--- Cluster Analysis ---")
    analysis = clean_customer_df.groupby('Cluster').agg({
        'Total_Spent': 'mean',
        'Frequency': 'mean',
        'Recency': 'mean'
    }).round(2)
    print(analysis)
    # Save final analysis report  to Excel
    analysis.to_excel("data/Business_Strategy_Report.xlsx")
    print("\n--- Business report saved as 'Business_Strategy_Report.xlsx'---")

    # 6. Save results
    clean_customer_df.to_excel("data/Final_Customer_Segments.xlsx", index=False)
    print("\n Project execution completed successfully!")

if __name__ == "__main__":
    main()