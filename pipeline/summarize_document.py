from langchain_groq import ChatGroq
from utils.data_ingestion_util import extract_text_from_pdf
from utils.logger import setup_logger
from model.cluster import cluster_texts
from model.summarization import summarize_texts
from model.embedding import get_embeddings_model

logger = setup_logger()

def summarize_document(file_path):
    """Extracts, clusters, and summarizes a document."""
    try:
        logger.info("Starting document summarization process.")
        embeddings = get_embeddings_model()
        llm = ChatGroq(model="llama3-8b-8192")
        
        texts = extract_text_from_pdf(file_path)
        clustered_texts = cluster_texts(texts, embeddings)
        summary = summarize_texts(clustered_texts, llm)
        
        logger.info("Document summarization completed successfully.")
        return summary
    except Exception as e:
        logger.error(f"Error summarizing document: {str(e)}")
        raise

if __name__ == "__main__":
    
    import os
    FILE_PATH = "uploads"

    if not os.path.exists(FILE_PATH):
        logger.error(f"File path {FILE_PATH} does not exist. Please check the path.")
        raise FileNotFoundError(f"File path {FILE_PATH} not found.")

    print(summarize_document(FILE_PATH))