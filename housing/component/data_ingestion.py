from email import message
from logging import raiseExceptions
from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit



class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            # raise Exception("Testing excepyion.")
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HousingException(e,sys)
        
    def download_housing_data(self):
        try:
            # Download the data.
            download_url = self.data_ingestion_config.dataset_download_url
            
            # Folder location to save the data.
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            
            # create the directory if it does not exist
            os.makedirs(tgz_download_dir, exist_ok=True)
            
            # File name of the downloaded data.
            housing_file_name = os.path.basename(download_url)
            
            # File path of the downloaded data.
            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)
            
            # Check if the file already exists.
            logging.info(f"Downloading data from {download_url} into directory {tgz_download_dir}")
            urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"[{tgz_file_path}] downloaded successfully.")
            
            return tgz_file_path
            
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            if os.makedirs(raw_data_dir, exist_ok=True):
                os.remove(raw_data_dir)
            
            os.makedirs(raw_data_dir, exist_ok=True)
            
            logging.info(f"Extracting {tgz_file_path} into {raw_data_dir} into directory {raw_data_dir}")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(raw_data_dir)
            logging.info(f"[{tgz_file_path}] extracted successfully.")
        
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            # Read the data.
            file_name = os.listdir(raw_data_dir)[0]
            
            # File path of the downloaded data.
            housing_file_path = os.path.join(raw_data_dir,file_name)
            
            # Read the data into pandas dataframe.
            logging.info(f"Reading csv file from [{housing_file_path}]")
            housing_data_frame = pd.read_csv(housing_file_path)
            
            housing_data_frame["income_cat"] = pd.cut(housing_data_frame["median_income"],
                                                      bins=[0,1.5,3.0,4.5,6.0,np.inf],
                                                      labels=["1","2","3","4","5"])
            
            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None
            
            split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
            
            for train_index,test_index in split.split(housing_data_frame,housing_data_frame["income_cat"]):
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"],axis=1)
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"],axis=1)
                
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(F"Exporting train data to [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)
                
            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(F"Exporting test data to [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)
                
            Data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            message=f"Data Ingestion completed successfully.")
            
            logging.info(f"Data Ingestion artifact: [{Data_ingestion_artifact}]")
            return Data_ingestion_artifact 
                   
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path =  self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise HousingException(e,sys) from e
        
        
    def __del__(self):
        logging.info(f"{'='*20} Data Ingestion completed successfully. {'='*20} \n\n")
            
        