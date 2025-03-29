from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"An error occurred during stage {STAGE_NAME}: {str(e)}")

    

