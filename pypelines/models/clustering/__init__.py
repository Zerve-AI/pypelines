from .kmeans import KMeansClustering, KMeansClusteringComparison
from .affinity_propagation import AffinityPropagationClustering, AffinityPropagationClusteringComparison
from .mean_shift import MeanShiftClustering, MeanShiftClusteringComparison
from .spectral_clustering import SpectralClustering, SpectralClusteringComparison
from .agglomerative import AgglomerativeClustering, AgglomerativeClusteringComparison
from .dbscan import DBSCANClustering, DBSCANClusteringComparison
from .hdbscan import HDBSCANClustering, HDBSCANClusteringComparison

models_clustering = {
    'KMeans': KMeansClustering,
    'AffinityPropagation': AffinityPropagationClustering,
    'MeanShift': MeanShiftClustering,
    'SpectralClustering': SpectralClustering,
    'AgglomerativeClustering': AgglomerativeClustering,
    'DBSCANClustering' : DBSCANClustering,
    'HDBSCANClustering':HDBSCANClustering
}

models_comparison_clustering = {
    'KMeans': KMeansClusteringComparison,
    'AffinityPropagation': AffinityPropagationClusteringComparison,
    'MeanShift': MeanShiftClusteringComparison,
    'SpectralClustering': SpectralClusteringComparison,
    'AgglomerativeClustering': AgglomerativeClusteringComparison,
    'DBSCANClustering' : DBSCANClusteringComparison,
    'HDBSCANClustering':HDBSCANClusteringComparison
}

models_clustering_default = {
    'KMeans': KMeansClustering,
    'AffinityPropagation': AffinityPropagationClustering,
    'MeanShift': MeanShiftClustering,
    'SpectralClustering': SpectralClustering,
    'AgglomerativeClustering': AgglomerativeClustering,
    'DBSCANClustering' : DBSCANClustering,
    'HDBSCANClustering':HDBSCANClustering
}

models_comparison_clustering_default = {
    'KMeans': KMeansClusteringComparison,
    'AffinityPropagation': AffinityPropagationClusteringComparison,
    'MeanShift': MeanShiftClusteringComparison,
    'SpectralClustering': SpectralClusteringComparison,
    'AgglomerativeClustering': AgglomerativeClusteringComparison,
    'DBSCANClustering' : DBSCANClusteringComparison,
    'HDBSCANClustering':HDBSCANClusteringComparison
}
