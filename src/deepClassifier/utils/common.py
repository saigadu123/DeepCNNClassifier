import os 
from box.exceptions import BoxValueError
import yaml 
from deepClassifier import logger 
import json 
import joblib 
from ensure import ensure_annotations 
from box import Configbox 
from pathlib import Path 
from typing import Any 

@ensure_annotations 
def read_yaml(path_to_yaml:Path)->Configbox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    pass

@ensure_annotations 
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    pass 

@ensure_annotations 
def save_json(path:Path,data:dict):
    """save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    pass

@ensure_annotations 
def load_json(path:Path)->Configbox:
    """load json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    pass 

@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    pass

@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    pass 

@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    pass 
