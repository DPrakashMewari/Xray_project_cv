from datetime import datetime
from typing import List

import torch


TIMESTAMP : datetime = datetime.now().strftime("%d_%m_%Y_%H")

ARTIFICAT_DIR: str = "artificats"

BUCKET_NAME: str ="xraylungimgss"

S3_DATA_FOLDER : str= "data"

CLASS_LABEL_1 :str = "NORMAL"

CLASS_LABEL_2 : str = "PNEUMONIA"