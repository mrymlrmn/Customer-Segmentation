import pandas as pd

class Cus_Segment_DataLoader:

    def __init__(self):
        self.df = None

    def data_loader(self, file_path=None):
        if file_path is None:
            file_path = "data/Online Retail.xlsx"
        self.df = pd.read_excel(file_path)
        print("Data loaded successfully from Excel.")
        return self.df
    