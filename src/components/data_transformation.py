'''
we are returning the raw train data & test data
'''
from src.logger import imp_logger
from src.exception import CustomException
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
import os
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_transform_object(self):

        try:
            num_col = ['reading_score','writing_score']

            num_pipelines = Pipeline(
                steps= [
                    ("imputer",SimpleImputer(strategy="median")),
                    ('scalar', StandardScaler()),
                ]
            )

            cat_col = ['gender',
                    'race_ethnicity',
                    'parental_level_of_education',
                    'lunch',
                    'test_preparation_course'
                    ]
            
            cat_pipeline = Pipeline(
                steps= [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoding',OneHotEncoder()),
                    ('scalar',StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipelines,num_col),
                    ('cat_pipeline',cat_pipeline,cat_col)
                ]
            )

            imp_logger.info('Completed num_columns and cat_columns pre-processing')
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
           
    def initiate_data_transformation(self,raw_train_data,raw_test_data):
        try:
            imp_logger.info('Initiated the data transformation')

            train_data_df = pd.read_csv(raw_train_data)
            test_data_df = pd.read_csv(raw_test_data)

            imp_logger.info('Loaded tarin and test data')
            output_col = 'math_score'

            input_features_train_df = train_data_df.drop(columns=[output_col], axis=1)
            output_features_train_df = train_data_df[output_col]

            input_features_test_df = test_data_df.drop(columns=[output_col],axis=1)
            output_features_test_df = test_data_df[output_col]

            imp_logger.info('from train & test data input & output features seperated')

            preprocessor_obj = self.get_transform_object()

            input_features_train_arr = preprocessor_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessor_obj.transform(input_features_test_df)

            train_arr = np.c_[input_features_train_arr,np.array(output_features_train_df)]
            test_arr = np.c_[input_features_test_arr,np.array(output_features_test_df)]

            imp_logger.info('Data prepared for model training')

            save_object (
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
