from langchain.chains.summarize import load_summarize_chain
from utils.logger import setup_logger

logger = setup_logger()

def summarize_texts(texts, llm, chain_type="stuff"):
    """Summarizes the given texts using the specified LLM."""
    try:
        logger.info("Summarizing texts using LLM.")
        checker_chain = load_summarize_chain(llm, chain_type=chain_type)
        summary = checker_chain.run(texts)
        logger.info("Text summarization completed successfully.")
        return summary
    except Exception as e:
        logger.error(f"Error summarizing texts: {str(e)}")
        raise
