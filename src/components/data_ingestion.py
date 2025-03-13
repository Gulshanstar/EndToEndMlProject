from src.logger import imp_logger
from src.exception import CustomException
from dataclasses import dataclass
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

@dataclass
class DataIngestionConfig:
    # It is joining the file name only not creating anything
    raw_data_file : str = os.path.join('artifact','data.csv')
    train_data_file : str = os.path.join('artifact', 'train.csv')
    test_data_file : str = os.path.join('artifact','test.csv')

class DataIngestion:
    def __init__(self):
        self.file_creation = DataIngestionConfig()

    def initiate_data_ingestion(self):
        imp_logger.info('Entered in the initiate data ingestion')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            imp_logger.info('Loaded the data')

            os.makedirs(os.path.dirname(self.file_creation.raw_data_file),exist_ok=True)

            df.to_csv(self.file_creation.raw_data_file, index=False, header=True)
            imp_logger.info('Data saved in artifact')

            imp_logger.info('Train test split started')
            train_df, test_df = train_test_split(df,test_size=0.20, random_state=42)

            train_df.to_csv(self.file_creation.train_data_file, index = False, header = True)
            imp_logger.info('Training data saved in artifcat')

            test_df.to_csv(self.file_creation.test_data_file, index = False, header = True)
            imp_logger.info('Test data saved in artifact and ingestion completed')

            return(
                self.file_creation.train_data_file,
                self.file_creation.test_data_file
            )
        except Exception as e:
            imp_logger.info('Some thing went wrong in data ingestion')
            raise CustomException(e, sys)
        

if __name__ == '__main__':
    objIngestion = DataIngestion()
    objIngestion.initiate_data_ingestion()
        
