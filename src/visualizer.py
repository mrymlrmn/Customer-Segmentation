import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

class Cus_Segment_Visualizer:
    def __init__(self):
        sns.set(style='whitegrid')

    def plot_elbow_method(self,scaled_data):
        wcss = []
        for i in range(1,11):
            kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
            kmeans.fit(scaled_data)
            wcss.append(kmeans.inertia_)

        plt.figure(figsize=(10, 6))
        plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='b')
        plt.title('The Elbow Method ', fontsize=15)
        plt.xlabel('(Number of Clusters)', fontsize=12)
        plt.ylabel('WCSS', fontsize=12)

        plt.annotate('Break point(Elbow)', xy=(3, wcss[2]), xytext=(5, wcss[2]+20000),
                     arrowprops=dict(facecolor='black', shrink=0.05))
        
        # Save the plot as an image file
        plt.savefig('elbow_report.png',dpi=300,bbox_inches='tight')
        plt.show()

