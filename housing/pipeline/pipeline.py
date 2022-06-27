from housing.component.data_ingestion import DataIngestion
from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HousingException

from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact

import os,sys

class Pipeline:
    def __init__(self,config:Configuration = Configuration()) -> None:
        try:
            # logging.info(f"{'='*20}Pipeline log started.{'='*20} ")
            self.config = config
            
        except Exception as e:
            raise HousingException(e,sys) from e
        
        def strat_data_ingestion(self) -> DataIngestionArtifact:
            try:
                data_ingestion= DataIngestion(data_ingestion_config=self.config.data_ingestion_config())
                
                return data_ingestion.strat_data_ingestion()
            except Exception as e:
                raise HousingException(e,sys) from e
            
        def start_data_validation(self):
            pass
        
        def start_data_transformation(self):
            pass
        
        def start_model_trainer(self):
            pass
        
        def start_model_evaluation(self):
            pass    
        
        def start_model_pusher(self):
            pass
        
        def run_pipeline(self):
            try:
                #data ingestion
                data_ingestion_artifact = self.strat_data_ingestion()
                
                
                
            except Exception as e:
                raise HousingException(e,sys) from e