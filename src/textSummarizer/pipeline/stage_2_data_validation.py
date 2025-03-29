from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_validation_config = config.get_data_ingestion_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.download_file()
            data_validation.extract_zip_file()       