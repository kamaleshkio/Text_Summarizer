import os 
import sys
import logging
logging_str = "[%(asctime)s:  %(levelname)s: %(modules)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")
os.mkdir(log_dir, exist = True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[logging.FileHandler(log_filepath), 
              logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("Text Summarizer Logger")
