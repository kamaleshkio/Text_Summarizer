from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_2_data_validation import DataValidationPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"Error occurred during {STAGE_NAME} execution: {e}")
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"Error occurred during {STAGE_NAME} execution: {e}")
    raise e

