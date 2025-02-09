import logging
import os

def setup_logger():
    """Sets up and returns a logger for tracking events."""

    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR) 
    werkzeug_logger.propagate = False

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, "app.log")

    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
        level=logging.INFO
    )

    logger = logging.getLogger("DocumentSummarizer")
    return logger

logger = setup_logger()
