from langchain_community.document_transformers import EmbeddingsClusteringFilter
from utils.logger import setup_logger

logger = setup_logger()

def cluster_texts(texts, embeddings, num_clusters=5):
    """
    
    Clusters text documents using embeddings.
    
    Args:
        texts (list): List of texts to cluster.
        embeddings (HuggingFaceBgeEmbeddings): The embeddings model to use for clustering.
        num_clusters (int): The number of clusters to create. Defaults to 5.
    Returns:
        list: The clustered texts.
    Raises:
        Exception: If an error occurs during clustering.
        
    """
    try:
        logger.info("Clustering texts using embeddings.")
        filter = EmbeddingsClusteringFilter(embeddings=embeddings, num_clusters=num_clusters)
        clustered_texts = filter.transform_documents(documents=texts)
        logger.info("Text clustering completed successfully.")
        return clustered_texts
    except Exception as e:
        logger.error(f"Error clustering texts: {str(e)}")
        raise
