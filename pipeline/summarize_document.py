from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.data_ingestion_util import extract_text_from_pdf
from utils.logger import setup_logger
from model.cluster import cluster_texts
from model.summarization import summarize_texts
from model.embedding import get_embeddings_model
from dotenv import load_dotenv
from rich import print
import os

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
# print(GEMINI_API_KEY)

logger = setup_logger()

def summarize_document(file_path):
    """
    
    Extracts, clusters, and summarizes a document. 

    Describe:
    This function extracts text from a document, clusters the text, and summarizes the text using a language model.
    The function uses the following steps:
    1. Extract text from the document.
    2. Cluster the text using embeddings.
    3. Summarize the text using a language
    model.

    Args:
        file_path (str): The path to the document to summarize.

    Returns:
        str: The summarized text.

    Raises:
        Exception: If an error occurs during summarization.


    """
    try:
        logger.info("Starting document summarization process.")
        embeddings = get_embeddings_model()


        # llm = ChatGroq(model="llama3-8b-8192")

        llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
        
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