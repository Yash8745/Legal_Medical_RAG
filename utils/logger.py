import logging
import os

SUCCESS = 25  # Between INFO (20) and WARNING (30)
logging.addLevelName(SUCCESS, "SUCCESS")

def success(self, message, *args, **kwargs):
    """
    Custom logging method for success messages.

    Args:
        message (str): The message to log.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    
    """
    if self.isEnabledFor(SUCCESS):
        self._log(SUCCESS, message, args, **kwargs)

# Add the success method to the Logger class
logging.Logger.success = success

def setup_logger():
    """
    
    Sets up and returns a logger for tracking events.

    Returns:
        Logger: The logger object.

    """

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
