from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import os
import sys
from sklearn.model_selection import train_test_split
import pandas as pd



#initialize data ingestion comfiguration


@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")

##creting class for data ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Starts')
        try:
            df = pd.read_csv(os.path.join('notebooks/data','cleaned_data.csv'))
            logging.info('Dataset Read as Pandas Datraframe')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Train Test split straing")
            train_set,test_set = train_test_split(df,test_size=0.20)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            logging.info("Ingestion of Data Completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )        
        

        except Exception as e:
            logging.info('Error ocuured in Data Ingestion Process')
            raise CustomException(e,sys)
        



#testing the Data Ingestion File

if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()