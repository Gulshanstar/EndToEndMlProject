import logging
from datetime import datetime
import os
# this file must be in logs folder
log_file_name = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_folder_dir = os.path.join(os.getcwd(),'logs')
print(logs_folder_dir)
os.makedirs(logs_folder_dir,exist_ok=True)
complete_path = os.path.join(logs_folder_dir,log_file_name)

logging.basicConfig(
    filename= complete_path,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(filename)s:%(lineno)d - %(message)s',
    level=logging.INFO
)

if __name__ =='__main__':
    logging.info('logging has started')