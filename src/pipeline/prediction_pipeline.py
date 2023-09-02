import os
import sys
from src.logger import logging 
from src.exception import CustomException
from dataclasses import dataclass


@dataclass
class PredictionPipelineConfig:
    model_path: str
    

class PredictionPipeline:
    def __init__(self, model_path:str ):
