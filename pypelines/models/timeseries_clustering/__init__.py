from .kmeans_ts_clustering import KMeansTSClustering, KMeansTSClusteringComparison
from .kmedoids_ts_clustering import KMediodsTSClustering, KMediodsTSClusteringComparison
from .kshapes_ts_clustering import KShapesTSClustering, KShapesTSClusteringComparison



models_ts_clustering = {
    'KMeans_TS': KMeansTSClustering,
    'KMedoids_TS': KMediodsTSClustering,
    'KShapes_TS': KShapesTSClustering
}

models_comparison_ts_clustering = {
    'KMeans_TS': KMeansTSClusteringComparison,
    'KMedoids_TS': KMediodsTSClusteringComparison,
    'KShapes_TS': KShapesTSClusteringComparison
}

models_ts_clustering_default = {
    'KMeans_TS': KMeansTSClustering,
    'KMedoids_TS': KMediodsTSClustering,
    'KShapes_TS': KShapesTSClustering
}


models_comparison_ts_clustering_default = {
    'KMeans_TS': KMeansTSClusteringComparison,
    'KMedoids_TS': KMediodsTSClusteringComparison,
    'KShapes_TS': KShapesTSClusteringComparison
}