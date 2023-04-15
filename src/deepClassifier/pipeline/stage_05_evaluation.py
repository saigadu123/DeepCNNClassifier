
from deepClassifier import logger
from deepClassifier.components import Evaluation
from deepClassifier.config import ConfigurationManager


STAGE_NAME = "Evaluation Stage"

def main():
    config = ConfigurationManager()
    val_config = config.get_evaluation_config()
    evaluation = Evaluation(config=val_config)
    evaluation.evaluation()
    evaluation.save_score()



if __name__ == "__main__":
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e