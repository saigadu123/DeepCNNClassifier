from deepClassifier.components import DataIngestion
from deepClassifier.config import ConfigurationManager
from deepClassifier import logger

STAGE_NAME = "Data Ingestion stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>")
        main()
        logger.info(f"<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e 