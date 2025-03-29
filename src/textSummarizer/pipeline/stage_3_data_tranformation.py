from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
            cconfig = ConfigurationManager()
            data_transformation_config = ConfigurationManager().get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()