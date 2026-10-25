import os
import sys
from src.ML_project.logger import logging
from src.ML_project.exception import CustomException
import pandas as pd
from src.ML_project.utils import read_data_from_sql
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")
    train_data_path: str = os.path.join("artifacts", "train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self, config: DataIngestionConfig):
        logging.info("Starting data ingestion process.")
        try:
            logging.info("Reading from SQL Database")
            # Read the raw data from the source
            df = read_data_from_sql()
            logging.info(f"Raw data read successfully from SQL database.")

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            # Save the raw data to the specified path
            df.to_csv(self.config.raw_data_path, index=False,header=True)
            logging.info(f"Raw data saved to {self.config.raw_data_path}.")

            # Split the data into training and testing sets (80-20 split)
            train_df,test_df = train_test_split(df, test_size=0.2, random_state=42)
            # Save the training and testing data to their respective paths
            train_df.to_csv(self.config.train_data_path, index=False)
            logging.info(f"Training data saved to {self.config.train_data_path}.")
            test_df.to_csv(self.config.test_data_path, index=False)
            logging.info(f"Testing data saved to {self.config.test_data_path}.")

        except Exception as e:
            logging.error("Error occurred during data ingestion.")
            raise CustomException(e, sys)