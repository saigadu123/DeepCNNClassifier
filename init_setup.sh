echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"
conda create -p env python==3.8 -y
echo [$(date)]: "activating the environment"
source activate ./env
echo [$(date)]: "installing the dev requirements"
pip install --user -r requirements_dev.txt
echo [$(date)]: "END"