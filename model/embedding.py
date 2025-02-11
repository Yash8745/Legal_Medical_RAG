from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from utils.logger import setup_logger

logger = setup_logger()

def get_embeddings_model(model_name="BAAI/bge-base-en-v1.5", device="cuda"):
    """
    Initializes and returns the embeddings model.
    
    Args:
        model_name (str): The name of the model to use. Defaults to "BAAI/bge-base-en-v1.5".
        device (str): The device to use for the model. Defaults to "cuda".

    Returns:
        HuggingFaceBgeEmbeddings: The embeddings model.

    Raises:
        Exception: If an error occurs during initialization.
    """
    try:
        logger.info("Initializing embeddings model.")
        encode_kwargs = {"normalize_embeddings": True}
        embeddings = HuggingFaceBgeEmbeddings(model_name=model_name, encode_kwargs=encode_kwargs)
        logger.info("Embeddings model initialized successfully.")
        return embeddings
    except Exception as e:
        logger.error(f"Error initializing embeddings model: {str(e)}")
        raise