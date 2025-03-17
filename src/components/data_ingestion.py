from src.logger import imp_logger
from src.exception import CustomException
from dataclasses import dataclass
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
from data_transformation import DataTransformation
from model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    # It is joining the file name only not creating anything
    raw_data_file : str = os.path.join('artifacts','data.csv')
    train_data_file : str = os.path.join('artifacts', 'train.csv')
    test_data_file : str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config_obj = DataIngestionConfig()

    def initiate_data_ingestion(self):
        imp_logger.info('Entered in the initiate data ingestion')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            imp_logger.info('Loaded the data')

            os.makedirs(os.path.dirname(self.data_ingestion_config_obj.raw_data_file),exist_ok=True)

            df.to_csv(self.data_ingestion_config_obj.raw_data_file, index=False, header=True)
            imp_logger.info('Data saved in artifact')

            imp_logger.info('Train test split started')
            train_df, test_df = train_test_split(df,test_size=0.20, random_state=42)

            train_df.to_csv(self.data_ingestion_config_obj.train_data_file, index = False, header = True)
            imp_logger.info('Training data saved in artifcat')

            test_df.to_csv(self.data_ingestion_config_obj.test_data_file, index = False, header = True)
            imp_logger.info('Test data saved in artifact and ingestion completed')

            return(
                self.data_ingestion_config_obj.train_data_file,
                self.data_ingestion_config_obj.test_data_file
            )
        except Exception as e:
            imp_logger.info('Some thing went wrong in data ingestion')
            raise CustomException(e, sys)
        

if __name__ == '__main__':
    objIngestion = DataIngestion()
    raw_train_data, raw_test_data = objIngestion.initiate_data_ingestion()

    data_tansformation_obj = DataTransformation()
    train_arr, test_arr, pre = data_tansformation_obj.initiate_data_transformation(raw_train_data,raw_test_data)

    model_trainer_obj = ModelTrainer()
    model_trainer_obj.initiate_model_training(train_arr,test_arr)

        
