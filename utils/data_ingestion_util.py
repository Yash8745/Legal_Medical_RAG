from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from utils.logger import setup_logger

logger = setup_logger()

def extract_text_from_pdf(file_path, chunk_size=2000, chunk_overlap=0):
    """Loads and splits text from a PDF file."""
    try:
        logger.info(f"Extracting text from PDF: {file_path}")
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        texts = text_splitter.split_documents(pages)
        logger.info("Text extraction completed successfully.")
        return texts
    except Exception as e:
        logger.error(f"Error extracting text: {str(e)}")
        raise