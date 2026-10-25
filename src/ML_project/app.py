from src.ML_project.logger import logging
from src.ML_project.exception import CustomException
import sys
from src.ML_project.components.data_ingestion import DataIngestion, DataIngestionConfig



if __name__ == "__main__":
    logging.info("Starting the ML Project application...")
    # Add your application logic here
    logging.info("ML Project application finished.")

    try:
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion(config=data_ingestion_config)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)