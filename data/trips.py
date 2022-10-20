import os
import json

import numpy as np
import pandas as pd

def load_month_data(file):
    """
    Extracts the data for a single month from a file.
    """
    with open(file) as f:
        data = json.load(f)
    return pd.DataFrame(data['data']['trips'])