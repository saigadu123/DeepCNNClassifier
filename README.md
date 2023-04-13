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






