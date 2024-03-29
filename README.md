# Deep Classifier project

## Template Creation for the project

step-1 => Create .gitignore file with python template

step-2 => Create License file

step-3 => Create template.py file to create all required files in the directory

step-4 => In setup.py file we create the setup

step-5 => In setup.cfg file we create the setup configuration

step-6 => In pyproject.toml file build system

step-7 => Fill the requirements_dev.txt the packages which are useful for only development

step-8 => Fill the requirements.txt the packages which are useful for production

step-9 => Fill the tox.ini file to create test environments

step-10 => Create environments using init_setup files

step-11 => Add the common.py file in utils folder 

step-12 => Add logger to the deepClassifier package in __init__.py file


## Workflow 

1. Update config.yaml

2. Update secrets.yaml [Optional]

3. Update params.yaml

4. Update the entity

5. Update the Configuration manager in src config

6. Update the components

7. Update the pipeline

8. Test run pipeline stage

9. Run tox for testing your package

10. Update the dvc.yaml

11. run "dvc repro" for running all the stages in pipeline


![img](https://raw.githubusercontent.com/saigadu123/DeepCNNClassifier/master/docs/images/Project%20structure.png)




## After training the model to check the tensorboard use the command

python -m tensorboard.main --logdir=path_to_log_directory

In this case path_to_log_directory = artifacts/prepare_callbacks/tensorboard_log_dir/


# DVC(Data Version Control)

1. dvc init (To initialize the dvc)

2. dvc repro (To run the pipeline)




# Commands to run mlflow server in local system
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./artifacts \
--host 127.0.0.1 -p 8080

step-1 : set the environment variable | Get it from dagshub -> remote tab -> mlflow tab 

MLFLOW_TRACKING_URI=https://dagshub.com/saigadu123/DeepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=saigadu123 \
MLFLOW_TRACKING_PASSWORD=bccea19a008f0ae53e36f39d62e73e9c58465616 \

step-2: install mlflow

step-3: set remote URI

step-4: Use context manager of mlflow to start run and then log metrics, params and model

# Building the docker Image

command-1 : docker build -t pred_service . (To build the Image)

command-2 : docker images (To check the existing images)

command-3 : docker run -p 8501:8501 pred_service(Image name) => (To run the docker image)









