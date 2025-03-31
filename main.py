from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_2_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.stage_3_data_tranformation import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_4_model_trainer import ModelTrainertrainingPipeline
from src.textSummarizer.pipeline.stage_5_model_evaluation import ModelEvaluationPipeline  
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


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_traansformation = DataTransformationPipeline()
    data_traansformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"Error occurred during {STAGE_NAME} execution: {e}")
    raise e


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_traansformation = ModelTrainertrainingPipeline()
    data_traansformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"Error occurred during {STAGE_NAME} execution: {e}")
    raise e



STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_traansformation = ModelEvaluationPipeline()
    data_traansformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(f"Error occurred during {STAGE_NAME} execution: {e}")
    raise e