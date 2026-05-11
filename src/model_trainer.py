from sklearn.cluster import KMeans

class Cus_Segment_Model:
    def __init__(self, n_clusters=3):
        """
        Initialize the trainer with the number of clusters.
        Default is 3 based on our Elbow Method analysis.
        """
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=self.n_clusters, init='k-means++', random_state=42)

    def train(self, scaled_data):
        """
        Fits the K-Means model and returns the cluster labels.
        """
        return self.model.fit_predict(scaled_data)

    def get_model_stats(self):
        """
        Returns the inertia (sum of squared distances) of the model.
        """
        return self.model.inertia_