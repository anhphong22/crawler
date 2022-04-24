import os
import json
import logging
import pandas as pd

def get_logger(name, level = 10):
    """Get logger"""
    logger = logging.getLogger(name)
    logger.propagate = 0
    logger.setLevel(level)
    header = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(name)s %(filename)s[%(lineno)d]: %(message)s")
    header.setFormatter(formatter)
    logger.addHandler(header)
    return logger

def load_json(data_path):
    if os.path.exists(data_path):
        data = pd.read_json(data_path)
        get_logger(__name__).info(f'Load json file from {data_path}')
    else:
        raise IOError('Not found')
    return data
