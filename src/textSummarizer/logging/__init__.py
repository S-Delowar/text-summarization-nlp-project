import logging
import os
from datetime import datetime

logging_str = f"[%(asctime)s : %(levelname)s : %(name)s : line %(lineno)d - %(message)s]"
logging_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

log_file_path = os.path.join(logs_dir, logging_file_name)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers= [
        logging.StreamHandler(),
        logging.FileHandler(log_file_path)
    ]
)

logger = logging.getLogger("textSummarizerLogger")