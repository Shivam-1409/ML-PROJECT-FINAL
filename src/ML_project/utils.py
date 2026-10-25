import os
import sys
from src.ML_project.logger import logging
from src.ML_project.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()  # Load environment variables from .env file

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_data_from_sql():
    """
    Reads data from a SQL database using the provided query.

    Args:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: The data read from the SQL database.
    """
    logging.info(f"Attempting to read data from SQL database")
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info(f"Successfully connected to the SQL database")
        df = pd.read_sql_query("SELECT * FROM college_data", connection)
        print(df.head())
        connection.close()
        return df
    except Exception as e:
        logging.error(f"Error occurred while reading data from SQL: {e}")
        raise CustomException(e, sys)