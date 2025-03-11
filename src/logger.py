"""
During execution logging the details 
"""

import logging
import os
from datetime import datetime

# log_file_name = f"{datetime.now().strftime('%m/%d/%y,%H:%M:%S')}.log"
# log_dir = os.path.join(os.getcwd(),'logs')

# os.makedirs('logs',exist_ok=True)
# file_path = os.path.join(log_dir,log_file_name)

# Generate log file name with correct formatting
log_file_name = f"{datetime.now().strftime('%m-%d-%y_%H-%M-%S')}.log"

# Create logs directory and file path
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists
file_path = os.path.join(log_dir, log_file_name)

print("Log File Path:", file_path)

logging.basicConfig(
    filename= file_path,
    format="%(asctime)s - %(levelname)s - [%(name)s] - %(filename)s:%(lineno)d - %(message)s",
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('logging started')
